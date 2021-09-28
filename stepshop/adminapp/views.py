from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from adminapp.forms import ProductCategoryCreateForm, ProductCategoryEditForm, ProductEditForm
from authapp.forms import ShopUserRegisterForm, ShopUserEditForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    title = 'админка | пользователи'

    user_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    context = {
        'title': title,
        'objects': user_list,
    }

    return render(request, 'adminapp/users.html', context)


def user_create(request):
    title = 'админка | создать пользователя'

    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)

        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin_staff:users'))

    else:
        user_form = ShopUserRegisterForm()

    context = {
        'title': title,
        'user_form': user_form,
    }

    return render(request, 'adminapp/users/user_create.html', context)


def user_update(request, pk):
    title = 'админка | редактировать пользователя'

    edit_user = get_object_or_404(ShopUser, id=pk)

    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=edit_user)

        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin_staff:users'))

    else:
        edit_form = ShopUserEditForm(instance=edit_user)

    context = {
        'title': title,
        'edit_form': edit_form,
        'edit_user': edit_user,
    }

    return render(request, 'adminapp/users/user_update.html', context)


def user_delete(request, pk):
    title = 'админка | удаление пользователя'

    user = get_object_or_404(ShopUser, id=pk)

    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('admin_staff:users'))

    context = {
        'title': title,
        'user_to_delete': user,
    }

    return render(request, 'adminapp/users/user_delete.html', context)


@user_passes_test(lambda u: u.is_staff)
def categories(request):
    title = 'админка | категории'

    categories_list = ProductCategory.objects.all()

    context = {
        'title': title,
        'objects': categories_list,
    }

    return render(request, 'adminapp/categories.html', context)


def category_create(request):
    title = 'админка | создать категорию'

    if request.method == 'POST':
        category_form = ProductCategoryCreateForm(request.POST, request.FILES)

        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('admin_staff:categories'))

    else:
        category_form = ProductCategoryCreateForm()

    context = {
        'title': title,
        'category_form': category_form,
    }

    return render(request, 'adminapp/categories/category_create.html', context)


def category_update(request, pk):
    title = 'админка | редактировать категорию'

    edit_category = get_object_or_404(ProductCategory, id=pk)

    if request.method == 'POST':
        edit_form = ProductCategoryEditForm(request.POST, request.FILES, instance=edit_category)

        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin_staff:categories'))

    else:
        edit_form = ProductCategoryEditForm(instance=edit_category)

    context = {
        'title': title,
        'edit_form': edit_form,
        'edit_category': edit_category,
    }

    return render(request, 'adminapp/categories/category_update.html', context)


def category_delete(request, pk):
    title = 'админка | удаление категории'

    category = get_object_or_404(ProductCategory, id=pk)

    if request.method == 'POST':
        category.is_active = False
        category.save()
        return HttpResponseRedirect(reverse('admin_staff:categories'))

    context = {
        'title': title,
        'category_to_delete': category,
    }

    return render(request, 'adminapp/categories/category_delete.html', context)


@user_passes_test(lambda u: u.is_staff)
def products(request, pk):
    title = 'админка | продукты'

    category = get_object_or_404(ProductCategory, id=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    context = {
        'title': title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/products.html', context)


def product_read(request, pk):
    title = 'админка | продукты подробнее'

    product = get_object_or_404(Product, id=pk)

    context = {
        'title': title,
        'product': product,
    }

    return render(request, 'adminapp/product/product_read.html', context)


def product_create(request, pk):
    title = 'админка | создать продукт'

    category = get_object_or_404(ProductCategory, id=pk)

    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES)

        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('admin_staff:products', args=[pk]))
    else:
        product_form = ProductEditForm(initial={'category': category})

    context = {
        'title': title,
        'create_form': product_form,
        'category': category,
    }

    return render(request, 'adminapp/product/product_create.html', context)


def product_update(request, pk):
    title = 'админка | редактировать продукт'

    edit_product = get_object_or_404(Product, id=pk)

    if request.method == 'POST':
        edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)

        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin_staff:products', args=[edit_product.category.pk]))
    else:
        edit_form = ProductEditForm(instance=edit_product)

    context = {
        'title': title,
        'update_form': edit_form,
        'product': edit_product,
    }

    return render(request, 'adminapp/product/product_update.html', context)


def product_delete(request, pk):
    title = 'админка | удалить продукт'

    product = get_object_or_404(Product, id=pk)

    if request.method == 'POST':
        product.is_active = False
        product.save()
        return HttpResponseRedirect(reverse('admin_staff:products', args=[product.category.pk]))

    context = {
        'title': title,
        'product_to_delete': product,
    }

    return render(request, 'adminapp/product/product_delete.html', context)
