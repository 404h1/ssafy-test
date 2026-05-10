from django.contrib import messages     # Message Framework (Flash Message)
from django.shortcuts import render, redirect

from .forms import ContactForm, ProductForm, BaseForm, ExtendedForm, WidgetForm, MyForm
from .models import Product


# Create your views here.
def form1(request):
    form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, 'formsapp/form1.html', context)


def form2(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            # form.save()

            # Multiple ChoiceField 실습에서 해제
            product = form.save(commit=False)  # 저장하지 않고 인스턴스 반환
            print(f'cleaned_data: {form.cleaned_data}')  # cleaned_data 확인
            print(f'cleaned_data 타입: {type(form.cleaned_data)}')  # cleaned_data 타입 확인

            category_values = form.cleaned_data.get('category', [])
            category_string = ','.join(category_values)  # 카테고리 데이터를 콤마로 구분된 문자열로 변환
            product.category = category_string
            product.save()

            # Message Framework (Flash Message)
            messages.success(request, f"제품 '{product.name}'이(가) 성공적으로 저장되었습니다!")  
            return redirect('formsapp:form2')
    else:
        form = ProductForm()

    # 저장된 제품 목록 가져오기
    products = Product.objects.all().order_by('-pk')[:5]

    context = {
        'form': form,
        'products': products,
    }

    return render(request, 'formsapp/form2.html', context)


def form3(request):
    form = BaseForm()
    context = {
        'form': form,
    }
    return render(request, 'formsapp/form3.html', context)


def form4(request):
    form = ExtendedForm()
    context = {
        'form': form,
    }
    return render(request, 'formsapp/form4.html', context)


def form5(request):
    form = WidgetForm()
    context = {
        'form': form,
    }
    return render(request, 'formsapp/form5.html', context)


def my_form(request):
    if request.method == 'POST':
        print('\n## 전달되는 Color 값 \n', request.POST, '\n######\n')

    form = MyForm()
    context = {
        'form': form,
    }
    return render(request, 'formsapp/my_form.html', context)
