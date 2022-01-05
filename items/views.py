from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Item, Category
from .forms import ItemForm


def all_items(request):
    items = Item.objects.all()
    if 'category' in request.GET: 
            category = request.GET['category'].split(',')
            items = items.filter(category__name__in=category)
            category = Category.objects.filter(name__in=category)[0]
            template = 'items/all_items.html'
            context = {
                'items': items,
                'category': category,
            }
            return render(request, template, context)
    else:
        items = list(Item.objects.all())
        def sort_item(item):
            return item.name
        items.sort(key=sort_item)
        all_products_category = 'All Products'
    template = 'items/all_items.html'
    context = {
        'items': items,
        'all_products_category': all_products_category,
    }
    return render(request, template, context)


def item_info(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    category = item.category
    similar_items = Item.objects.all().filter(category=category).exclude(id=item_id)
    template = 'items/item_info.html'
    context = {
        'item': item,
        'similar_items': similar_items,
    }
    return render(request, template, context)


def add_item(request):
    form = ItemForm()
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            return redirect('item_info', item_id=item.id)
    template = 'items/add_item.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def edit_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    form = ItemForm(instance=item)
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES, instance=item)
        print('form is valid', form.is_valid())
        print(request.POST)
        print(form)
        print(dir(form))
        print(form.data)
        if form.is_valid():
            form.instance.name = request.POST.get('name')
            item = form.save()
            item_id = item.id
            return redirect('item_info', item_id=item.id)
    template = 'items/edit_item.html'
    context = {
        'form': form,
        'item': item,
    }
    return render(request, template, context)


def delete_item(request, item_id):
    product = get_object_or_404(Item, pk=item_id)
    product.delete()
    return redirect(reverse('all_items'))