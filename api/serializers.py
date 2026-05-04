from rest_framework import serializers
from projects.models import Project, Technology
from blog.models import Article, Tag

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ['id', 'name', 'color']

class ProjectSerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer(many=True, read_only=True)
    category_display = serializers.CharField(source='get_category_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    features_list = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'slug', 'category', 'category_display',
            'status', 'status_display', 'description_short', 'description_full',
            'architecture', 'database_info', 'features_list', 'technologies',
            'thumbnail', 'github_url', 'demo_url', 'icon', 'is_featured',
        ]

    def get_features_list(self, obj):
        return obj.get_features_list()

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug', 'color']

class ArticleSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = [
            'id', 'title', 'slug', 'excerpt', 'content', 'tags',
            'icon', 'read_time', 'views_count', 'published_at',
        ]