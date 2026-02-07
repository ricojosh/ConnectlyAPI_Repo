from posts.models import Post
from django.contrib.auth.models import User 
from posts.models import Post, User

class PostFactory:
    @staticmethod
    def create_post(post_type, title, author_id, content='', metadata=None):
        if post_type not in dict(Post.POST_TYPES):
            raise ValueError("Invalid post type")

        try:
            author = User.objects.get(id=author_id)
        except User.DoesNotExist:
            raise ValueError("Author not found")

        # Validation logic to prevent server crashes
        if post_type == 'image' and (metadata is None or 'file_size' not in metadata):
            raise ValueError("Image posts require 'file_size' in metadata")
        if post_type == 'video' and (metadata is None or 'duration' not in metadata):
            raise ValueError("Video posts require 'duration' in metadata")

        return Post.objects.create(
            title=title,
            content=content,
            author=author,
            post_type=post_type,
            metadata=metadata or {}
        )
