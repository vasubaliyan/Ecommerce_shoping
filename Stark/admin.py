from django.contrib import admin

from Stark.views import checkout
from.models import *

admin.site.register((MainCategory,SubCategory,Brand,Product
,Seller,Buyer, Wishlist,Checkout,Subscribe,
                    Contact,))
                    
