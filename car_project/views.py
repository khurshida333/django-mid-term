# from django.shortcuts import render
# from posts.models import Post
# from categories.models import Category
# # Create your views here.

# def home(request, category_slug=None):
#     data = Post.objects.all()
#     if category_slug:
#         category = Category.objects.get(slug=category_slug)
#         data = Post.objects.filter(category=category)
#     categories = Category.objects.all()

#     return render(request, 'home.html',{'data': data , 'category': categories}) 

from django.shortcuts import render
from cars.models import Car
from brands.models import Brand

def home(request, category_slug=None):
    data_all = Car.objects.all()  # Get all posts
    total_posts_count = data_all.count()  # Count of all posts
    
    if category_slug is not None:
        category = Brand.objects.get(slug=category_slug)
        data =Car.objects.filter(category=category)  # Filter posts by category
        filtered_posts_count = data.count()  # Count of filtered posts
    else:
        data = data_all  # If no category is selected, show all posts
        filtered_posts_count = total_posts_count  # Total count equals filtered count

    categories = Brand.objects.all()  # Get all categories
    
    return render(request, 'home.html', {
        'data': data, 
        'data_all': data_all,
        'category': categories, 
        'total_posts_count': total_posts_count,
        'filtered_posts_count': filtered_posts_count
    })