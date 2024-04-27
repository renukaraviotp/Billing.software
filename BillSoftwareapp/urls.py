#Multiuserbillingindia
from . import views
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

urlpatterns = [

    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('service', views.service, name='service'),
    path('register', views.register, name='register'),
    path('registercompany', views.registercompany, name='registercompany'),
    path('registerstaff', views.registerstaff, name='registerstaff'),
    path('login', views.login, name='login'),
    path('registeruser', views.registeruser, name='registeruser'),
    path('add_company', views.add_company, name='add_company'),
    path('staff_registraction', views.staff_registraction, name='staff_registraction'),
    path('homepage', views.homepage, name='homepage'),
    path('staffhome', views.staffhome, name='staffhome'),
    path('loginurl', views.loginurl, name='loginurl'),
    path('logout', views.logout, name='logout'),
    path('base', views.base, name='base'),
    path('profile', views.profile, name='profile'),
    path('editprofile/<int:pk>/', views.editprofile, name='editprofile'),
    path('edit_profilesave/<int:pk>/', views.edit_profilesave, name='edit_profilesave'),
    path('editstaffprofile', views.editstaffprofile, name='editstaffprofile'),
    path('edit_staffprofilesave/', views.edit_staffprofilesave, name='edit_staffprofilesave'),
    path('staffprofile', views.staffprofile, name='staffprofile'),
    path('add_item', views.add_item, name='add_item'),
    path('item_create_new', views.item_create_new, name='item_create_new'),
    path('view_item', views.view_item, name='view_item'),
    path('view_items/<int:pk>/', views.view_items, name='view_items'),
    path('edit_item/<int:pk>/', views.edit_item, name='edit_item'),
    path('update_item/<int:pk>/', views.update_item, name='update_item'),
    path('item_delete/<int:pk>/', views.item_delete, name='item_delete'),
    path('itemhistory/<int:pk>/', views.itemhistory, name='itemhistory'),
    path('item_unit_create', views.item_unit_create, name='item_unit_create'),
    path('ajust_quantity/<int:pk>/', views.ajust_quantity, name='ajust_quantity'),
    path('itemmodaladjust/<int:pk>/', views.itemmodaladjust, name='itemmodaladjust'),
    path('edititemmodaladjust/<int:pk>/<int:trans>', views.edititemmodaladjust, name='edititemmodaladjust'),
    path('update_adjusted_transaction/<int:pk>/<int:trans>', views.update_adjusted_transaction, name='update_adjusted_transaction'),
    path('transaction_delete/<int:pk>', views.transaction_delete, name='transaction_delete'),
    path('item_delete_openstock/<int:pk>',views.item_delete_openstock,name='item_delete_openstock'),
    
    path('add_debitnote',views.add_debitnote,name='add_debitnote'),
    path('add_parties', views.add_parties, name='add_parties'),
    path('save_parties', views.save_parties, name='save_parties'),
    path('parties_default', views.parties_default, name='parties_default'),
    path('create_debitnotes',views.create_debitnotes,name='create_debitnotes'),
    path('view_purchasedebit',views.view_purchasedebit,name='view_purchasedebit'),
    path('view_parties', views.view_parties, name='view_parties'),
    path('view_party/<int:id>', views.view_party, name='view_party'),
    path('saveitem',views.saveitem,name='saveitem'),
    path('itemdetail',views.itemdetail,name='itemdetail'),
    path('savecustomer1',views.savecustomer1,name='savecustomer1'),
    path('cust_dropdown1',views.cust_dropdown1,name='cust_dropdown1'),
    path('saveitem1',views.saveitem1,name='saveitem1'),
    path('item_dropdowns',views.item_dropdowns,name='item_dropdowns'),
    path('custdata1',views.custdata1,name='custdata1'),
    path('purchasebilldata',views.purchasebilldata,name='purchasebilldata'),
    path('get_bill_date',views.get_bill_date,name='get_bill_date'),
    path('bankdata1',views.bankdata1,name='bankdata1'),
    
    path('delete_debit/<int:id>',views.delete_debit,name='delete_debit'),
    path('details_debitnote/<int:id>/', views.details_debitnote, name='details_debitnote'),
    
    path('check_contact_exists',views.check_contact_exists,name='check_contact_exists'),
    path('check_email_exists',views.check_email_exists,name='check_email_exists'),
    path('check_hsn_exists',views.check_hsn_exists,name='check_hsn_exists'),

    path('edit_debitnote/<int:id>',views.edit_debitnote,name='edit_debitnote'),
    
    path('update_debitnote/<int:id>',views.update_debitnote,name='update_debitnote'),
    path('sharedebitToEmail/<int:id>',views.sharedebitToEmail,name='sharedebitToEmail'),
    
    # harikrishnan-------
    
    path('parties_add_page',views.parties_add_page,name='parties_add_page'),
    path('parties_table',views.parties_table,name='parties_table'),
    path('party_save',views.party_save,name='party_save'),
    path('party_delete/<int:pk>',views.party_delete,name='party_delete'),
    path('party_edit/<int:pk>/<str:id>',views.party_edit,name='party_edit'),
    path('party_update/<int:pk>',views.party_update,name='party_update'),
    path('parties_history/<int:pk>/<str:id>',views.parties_history,name="parties_history"),
    path('party_details/<int:pk>/<str:id>',views.party_details,name="party_details"),

    # end-----
    
    path('view_purchasebill', views.view_purchasebill, name='view_purchasebill'),
    path('add_purchasebill', views.add_purchasebill, name='add_purchasebill'),
    path('create_purchasebill', views.create_purchasebill, name='create_purchasebill'),
   
    path('savecustomer', views.savecustomer, name='savecustomer'),
    path('cust_dropdown', views.cust_dropdown, name='cust_dropdown'),
    path('item_dropdown', views.item_dropdown, name='item_dropdown'),
    path('itemdetails', views.itemdetails, name='itemdetails'),
    path('custdata',views.custdata,name='custdata'),
    path('show_purchasebill/<int:id>/', views.show_purchasebill, name='show_purchasebill'),
    path('edit_purchasebill/<int:id>',views.edit_purchasebill,name='edit_purchasebill'),
    path('update_purchasebill/<int:id>',views.update_purchasebill,name='update_purchasebill'),
    path('details_purchasebill/<int:id>',views.details_purchasebill,name='details_purchasebill'),
    path('history_purchasebill/<int:id>',views.history_purchasebill,name='history_purchasebill'),
    path('delete_purchasebill/<int:id>',views.delete_purchasebill,name='delete_purchasebill'), 
    path('history',views.history,name='history'),
    path('sharepdftomail/<int:id>',views.sharepdftomail,name="sharepdftomail"),
    path('import_purchase_bill',views.import_purchase_bill,name='import_purchase_bill'),
    path('billhistory',views.billhistory,name='billhistory'),
    path('save_item', views.save_item,name='save_item'),
    
    path('check_gstin_exists', views.check_gstin_exists, name='check_gstin_exists'),
    path('check_phone_number_exists/', views.check_phone_number_exists, name='check_phone_number_exists'),
    
    path('customerdata',views.customerdata,name='customerdata'),
    
    path('add_unit',views.add_unit,name='add_unit'),
    
    path('sales_invoice_home', views.sales_invoice_home, name='sales_invoice_home'),
    path('sales_invoice_list', views.sales_invoice_list, name='sales_invoice_list'),
    path('sales_invoice', views.sales_invoice, name='sales_invoice'),
    path('sales_invoice_add', views.sales_invoice_add, name='sales_invoice_add'),
    path('salesinvoice_add_parties', views.salesinvoice_add_parties, name='salesinvoice_add_parties'),
    path('sales_invoice_list', views.sales_invoice_list, name='sales_invoice_list'),
    path('salesinvoice_saveitem',views.salesinvoice_saveitem,name='salesinvoice_saveitem'),
    path('salesinvoice_item_dropdown',views.salesinvoice_item_dropdown,name='salesinvoice_item_dropdown'),
    path('save_sales_invoice', views.save_sales_invoice, name='save_sales_invoice'),
    path('edit_save_sales_invoice/<int:id>/', views.edit_save_sales_invoice, name='edit_save_sales_invoice'),
    path('delete_sales_invoice/<int:id>/', views.delete_sales_invoice, name='delete_sales_invoice'),
    path('salesinvoice_history/<int:id>/', views.salesinvoice_history, name='salesinvoice_history'),
    path('edit_salesinvoice/<int:id>/', views.edit_salesinvoice, name='edit_salesinvoice'),
    path('itemdata_salesinvoiceedit',views.itemdata_salesinvoiceedit,name='itemdata_salesinvoiceedit'),
    path('salesinvoice_template/<int:id>/', views.salesinvoice_template, name='salesinvoice_template'),
    path('salesinvoice_graph', views.salesinvoice_graph, name='salesinvoice_graph'),
    path('export_sales_invoices_to_excel', views.export_sales_invoices_to_excel, name='export_sales_invoices_to_excel'),
    path('import_invoice_data', views.import_invoice_data, name='import_invoice_data'),
    path('import_excel', views.import_excel, name='import_excel'),
    path('shareinvoiceToEmail/<int:id>/', views.shareinvoiceToEmail, name='shareinvoiceToEmail'),
    path('salesinvoice_savecustomer', views.salesinvoice_savecustomer, name='salesinvoice_savecustomer'),
    path('salesinvoice_add_unit', views.salesinvoice_add_unit, name='salesinvoice_add_unit'),
    path('salesinvoice_custdata',views.salesinvoice_custdata,name='salesinvoice_custdata'),
    path('check_unit_existence',views.check_unit_existence,name='check_unit_existence'),
    
    path('check_gst_exists',views.check_gst_exists,name='check_gst_exists'),
    
    path('history_debitnote/<int:id>',views.history_debitnote,name='history_debitnote'),
    path('debthistory',views.debthistory,name='debthistory'),

    ######Renuka T ########
    path('credit_add',views.credit_add,name='credit_add'),
    path('creditbilldata',views.creditbilldata,name='creditbilldata'),
    path('credit_bill_date',views.credit_bill_date,name='credit_bill_date'),
    path('saveparty',views.saveparty,name='saveparty'),
    path('party_dropdown',views.party_dropdown,name='party_dropdown'),
    path('savecredititem',views.savecredititem,name='savecredititem'),
    path('credititem_dropdown',views.credititem_dropdown,name='credititem_dropdown'),
    path('credit_save',views.credit_save,name='credit_save'),
    path('get_tax_rate/', views.get_tax_rate, name='get_tax_rate'),
    path('transactiontable',views.transactiontable,name='transactiontable'),
    path('edit_credit/<int:pk>',views.edit_credit,name='edit_credit'),
    path('update_creditnote/<int:pk>',views.update_creditnote,name='update_creditnote'),
    path('template1/<int:pk>',views.template1,name='template1'),
    path('template2/<int:pk>',views.template2,name='template2'),
    path('template3/<int:pk>',views.template3,name='template3'),
    path('credithistory/<int:pk>',views.credithistory,name='credithistory'),
    path('delete_credit/<int:pk>',views.delete_credit,name='delete_credit'),
    path('pdftomailcredit/<int:pk>',views.pdftomailcredit,name='pdftomailcredit'),
    path('partydata',views.partydata,name='partydata'),
    #End
    path('get_all_units',views.get_all_units,name='get_all_units'),
    
    path('saveitemc',views.saveitemc,name='saveitemc'),
    path('item_dropdownc',views.item_dropdownc,name='item_dropdownc'),
    
    path('check_email/', views.check_email, name='check_email'),
    
    path('edit_purchasebill/check_hsn', views.check_hsn, name='check_hsn'),
    path('edit_purchasebill/check_gstin', views.check_gstin, name='check_gstin'),
    path('edit_purchasebill/check_phone_number', views.check_phone_number, name='check_phone_number'),
    path('edit_purchasebill/check_mail', views.check_mail, name='check_mail'),
    
    path('add_unit1',views.add_unit1,name='add_unit1'),
    path('get_all_unit1',views.get_all_unit1,name='get_all_unit1'),
    path('check_unit_existence1',views.check_unit_existence1,name='check_unit_existence1'),
    # path('add_unit2',views.add_unit2,name='add_unit2'),
    
    path('saveitemcr',views.saveitemcr,name='saveitemcr'),
    path('item_dropdowncr',views.item_dropdowncr,name='item_dropdowncr'),
    path('check_phone_no',views.check_phone_no,name='check_phone_no'),
    path('check_emailc',views.check_emailc,name='check_emailc'),
    path('check_gstc',views.check_gstc,name='check_gstc'),
    path('check_unit',views.check_unit,name='check_unit'),
    path('check_unitc',views.check_unitc,name='check_unitc'),
    path('allunits',views.allunits,name='allunits'),
    path('allunitsc',views.allunitsc,name='allunitsc'),
    path('addunitc',views.addunitc,name='addunitc'),
    path('check_hsnc',views.check_hsnc,name='check_hsnc'),
    
    path('credithistoryc',views.credithistoryc,name='credithistoryc'),
    
    path('invoice_edit/<int:id>/', views.invoice_edit, name='invoice_edit'),
    path('sales_invoice_add/check_hsn_exist',views.check_hsn_exist,name='check_hsn_exist'),
    path('sales_invoice_add/check_gstin_exist', views.check_gstin_exist, name='check_gstin_exist'),
    path('sales_invoice_add/check_phone_number_exist', views.check_phone_number_exist, name='check_phone_number_exist'),
    path('sales_invoice_add/check_email_exist',views.check_email_exist,name='check_email_exist'),
    path('invoice_edit/editpage_savecustomer', views.editpage_savecustomer, name='editpage_savecustomer'),
    
    path('invoice_edit/check_phone_numbers', views.check_phone_numbers, name='check_phone_numbers'),
    path('invoice_edit/check_gstins', views.check_gstins, name='check_gstins'),
    path('invoice_edit/check_mails',views.check_mails,name='check_mails'),
    path('invoice_edit/check_hsns',views.check_hsns,name='check_hsns'),
    
    path('check_name_exists',views.check_name_exists,name='check_name_exists'),
    path('check_item_exists', views.check_item_exists, name='check_item_exists'),
    path('check_item', views.check_item, name='check_item'),
    
    path('check_itmname',views.check_itmname,name='check_itmname'),

    path('sales_report',views.sales_report,name='sales_report'),
    path('shareSalesReportsToEmail',views.shareSalesReportsToEmail, name='shareSalesReportsToEmail'),
    path('salesreport_graph',views.salesreport_graph, name='salesreport_graph'),
    
    path('getItemDetailsinvoice',views.getItemDetailsinvoice, name='getItemDetailsinvoice'),

    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)