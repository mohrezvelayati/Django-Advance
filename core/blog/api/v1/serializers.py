from rest_framework import serializers
from blog.models import Post, Category
from accounts.models import Profile

# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length = 255)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class PostSerializer(serializers.ModelSerializer):
    snippets = serializers.ReadOnlyField(source="get_snippets")
    relative_url = serializers.URLField(source="get_absolute_api_url", read_only=True)
    absolute_url = serializers.SerializerMethodField(method_name="get_absolute_url")
    category = serializers.SlugRelatedField(
        many=False, slug_field="name", queryset=Category.objects.all()
    )

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "title",
            "image",
            "content",
            "snippets",
            "category",
            "status",
            "absolute_url",
            "relative_url",
            "created_date",
            "published_date",
        ]
        read_only_fields = ["author"]

    def get_absolute_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj)

    def to_representation(self, instance):
        request = self.context.get("request")
        rep = super().to_representation(instance)
        rep["state"] = "list"
        if request.parser_context.get("kwargs").get("pk"):
            rep.pop("snippets", None)
            rep.pop("relative_url", None)
            rep.pop("absolute_url", None)
        else:
            rep.pop("content", None)
        rep["category"] = CategorySerializer(
            instance.category, context={"request": request}
        ).data
        return rep

    """
    def create(self, validated_data):
        validated_data['author'] = Profile.objects.get(user__id = self.context.get('request').user.id)
        return super().create(validated_data)
    """

    """
    def create(self, validated_data):
        # Get the user ID from the request context
        user_id = self.context.get('request').user.id

        # Get the profile of the user
        profile = Profile.objects.get(user__id=user_id)

        # Add the profile to the validated data
        validated_data['author'] = profile

        # Create the new object
        instance = super().create(validated_data)

        # Return the created object
        return instance"""
