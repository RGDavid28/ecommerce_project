from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class ProductPagination(PageNumberPagination):
 #   page_size               = 1
   page_query_param        = "p" #Page
   page_size_query_param   = "size"
   max_page_size           = 2
   last_page_strings       = "end"

class ProductLOPagination(LimitOffsetPagination):
   default_limit           = 2
   max_limit               = 3
   limit_query_param       = "records"
   offset_query_param      = "start"

class ProductCPagination(CursorPagination):
   page_size               = 1
   cursor_query_param      = "cur"
   ordering                = "title" #"-created"
