# Different API views in Django:

## 1. Function-Based Views (FBVs)

- You can use decorators to specify which HTTP methods the view should respond to.

```
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def example_view(request):
    if request.method == 'GET':
       ...
    elif request.method == 'POST':
        ...
```

## 2. Class-Based Views (CBVs)

-

```
from rest_framework.views import APIView

class ExampleAPIView(APIView):
    def get(self, request):
       ...
    def post(self, request):
        ...
```

## 3. Generic Views

- Generic views abstract common patterns, reducing boilerplate code.
- DRF provides several generic views for common operations like listing, creating, retrieving, updating, and deleting objects.

```
from rest_framework import generics

class MyModelListCreate(generics.ListCreateAPIView):
    ...
class MyModelDetail(generics.RetrieveUpdateDestroyAPIView):
    ...
```

## 4. ViewSets

- allow you to group related views into a single class.

- Instead of writing separate views for listing, creating, retrieving, updating, and deleting objects, you can encapsulate all these actions within a single ViewSet.

- (DRF) provides a powerful feature called routers that can automatically generate URL routes for all the actions defined in a ViewSet.

  - GET /api/books/ - List all books (maps to the list action)
  - POST /api/books/ - Create a new book (maps to the create action)
  - GET /api/books/{id}/ - Retrieve a specific book by ID (maps to the retrieve action)
  - PUT /api/books/{id}/ - Update a specific book by ID (maps to the update action)
  - PATCH /api/books/{id}/ - Partially update a specific book by ID (maps to the partial_update action)

```
from rest_framework import viewsets

class BookViewSet(viewsets.ModelViewSet):
    ...
```

```
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

```

### Types of ViewSets

- `ViewSet`: The most basic type, where you define your own methods.
- `ModelViewSet`: A ViewSet that provides default implementations for typical actions like list, create, retrieve, update, and destroy.
- `ReadOnlyModelViewSet`: A ViewSet that provides default implementations for read-only actions like list and retrieve.

## as_view()

- as_view() is typically used for all class-based views (CBVs) in Django.

- use the `as_view()` method to convert the class into a `callable view function` that Django's URL dispatcher can `recognize and route requests` to.

- When a `request matches` the specified `URL pattern`, Django calls the `as_view()` method to instantiate the CBV and `route the request` to the appropriate `method (get, post, etc.)` based on the HTTP method of the request.

- In `function-based views` (FBVs), you define a `Python function` to handle a particular `URL pattern` directly. Unlike `class-based views` (CBVs), there's no need to use a method like as_view() because a `function itself` is already `callable`.

# Authentication

- By setting permission_classes = [IsAuthenticated], Django REST framework automatically checks if the user is authenticated before allowing access to the view. If the user is not authenticated, a 401 Unauthorized response is returned automatically.

- authentication_classes = [TokenAuthentication]: This specifies that the view uses token-based authentication.
