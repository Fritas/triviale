from django.shortcuts import render

# Create your views here.
def index_render(request):
    return render(request, 'index.html')


def about_render(request):
    about = About('Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo')
    about.add_author(
        Person(
            first_name='Adriano',
            last_name='Damasceno da Silva Júnior',
            bibliography='Adriano is a student of teology degree.'
        )
    )
    about.add_author(
        Person(
            first_name='Nicholas',
            last_name='Fath Gomes',
            bibliography='Nicholas is a student of international relations and foreign trade.'
        )
    )
    about.add_contributor(
        Person(
            first_name='First Name',
            last_name='Last Name',
            bibliography='Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.'
        )
    )
    about.add_contributor(
        Person(
            first_name='First Name',
            last_name='Last Name',
            bibliography='Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.'
        )
    )
    about.add_contributor(
        Person(
            first_name='First Name',
            last_name='Last Name',
            bibliography='Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.'
        )
    )
    return render(request, 'about.html', {'about' : about})


def contact_render(request):
    contact = Contact(whatsapp='+55 ddd 00000-0000', email='contact@triviale.com.br')
    return render(request, 'contact.html', {'contact' : contact})

class Contact(object):


    def __init__(self, whatsapp, email):
        self.whatsapp = whatsapp
        self.email = email

class About(object):


    def __init__(self, site, authors=[], contributors=[]):
        self.site = site
        self.authors = authors
        self.contributors = contributors

    def add_author(self, author):
        self.authors.append(author)


    def add_contributor(self, contributor):
        self.contributors.append(contributor)


class Person(object):


    def __init__(self, first_name, last_name, bibliography):
        self.first_name = first_name
        self.last_name = last_name
        self.bibliography = bibliography
