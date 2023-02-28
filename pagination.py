from django.core.paginator import Paginator

def paginate(request,data_list,number):

    paginator = Paginator(data_list, number) # Show 25 contacts per page.
    page_number = request.GET.get('page',1) # for boxy pagination
    page_obj = paginator.get_page(page_number)
    return page_obj