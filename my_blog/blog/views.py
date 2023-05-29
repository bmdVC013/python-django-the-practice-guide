from django.shortcuts import render
from django.http import Http404

BLOG_MAPPER = {
    "first-blog": "This is my first blog",
    "second-blog": "This is my second blog",
    "third-blog": "This is my third blog",
}

# Create your views here.

def index(request):
    blog_names = list(BLOG_MAPPER.keys())

    return render(request, "blog/index.html", {
        "blog_names": blog_names
    })

def blog_detail(request, blog_name):
    try:
        blog_content = BLOG_MAPPER[blog_name]

        return render(request, "blog/blog-detail.html", {
            "content": blog_content,
            "blog_name": blog_name
        })
    except:
        raise Http404()