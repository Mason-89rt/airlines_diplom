# from fastapi import APIRouter
# from endpoints.models import company_information_view, company_web_site,company_name_rating,company_phone_email
# from db.DBmanager import base_manager
# router = APIRouter()
#
#
# def get_phone_email(company: company_phone_email):
#     res = base_manager.execute("select * from company_information where id=?", args=(company.phone,company.email, company.id), many=True)
#     return res
#
#
# def get_company_information():
#     res = base_manager.execute("select * from company_information", args=(), many=True)
#     if res:
#         company_list = [company_information_view(id=row[0], name=row[1], address=row[2], web_site=row[3], phone=row[4], email=row[5], rating=row[6], date_of_creation=row[7]) for row in res]
#         return company_list
#     else:
#         return None
#
#
# def post_company_information(company: company_information_view):
#     res = base_manager.execute("insert into company_information (id, name, address,web_site, phone, email, rating, date_of_creation,) values(?,?,?,?,?,?,?)", args=(company.id, company.name, company.address, company.web_site, company.phone, company.email, company.rating, company.date_of_creation))
#     return res
#
#
# def put_web_site(company: company_web_site):
#     res = base_manager.execute("update company_information set web_site=? where id=?", args=(company.web_site,))
#     return res
#
#
# def delete_web_site(company: company_web_site):
#     res = base_manager.execute("delete content from company_information where web_site=?", args=(company.web_site,))
#     return res
#
#
# def delete_rating(company: company_name_rating):
#     res = base_manager.execute("delete name from company_information where rating=?", args=(company.name, company.rating))
#     return res
#
#
# @router.get("/information/phone_email")
# def get_endpoint(endpoint: company_phone_email):
#     return get_phone_email(endpoint)
#
#
# @router.get("/information")
# def get_endpoint():
#     return get_company_information()
#
#
# @router.post("/information")
# def get_endpoint(endpoint: company_information_view):
#     return post_company_information(endpoint)
#
#
# @router.put("/information/web_site")
# def get_endpoint(endpoint: company_web_site):
#     return put_web_site(endpoint)
#
#
# @router.delete("/information/web_site")
# def get_endpoint(endpoint: company_web_site):
#     return delete_web_site(endpoint)
#
#
# @router.delete("/information/rating")
# def get_endpoint(endpoint: company_name_rating):
#     return delete_rating(endpoint)
