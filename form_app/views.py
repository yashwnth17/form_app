
from django.shortcuts import render, redirect
from form_app.forms import ProductForm
from form_app.models import Product



def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'product_for.html', {'form': form})


def product_list(request):
    products = Product.objects.all()

    return render(
        request,
        'show_details.html',
        {'products': products}
    )


def search_product(request):
    query = request.GET.get('q', '').strip()

    products = Product.objects.filter(name__icontains=query)
    

    return render(
        request,
        'search.html',
        {'products': products, 'query': query}
    )