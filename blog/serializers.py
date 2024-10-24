from rest_framework import serializers
from .models import Post, Category, Section


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['subtitle', 'content']


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    sections = SectionSerializer(many=True)
    image = serializers.ImageField(required=False)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content',
                  'created_at', 'category', 'sections', 'image']
