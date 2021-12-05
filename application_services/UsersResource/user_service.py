from application_services.BaseApplicationResource import BaseRDBApplicationResource
import database_services.RDBService as d_service

from database_services.RDBService import RDBService

class UserResource(BaseRDBApplicationResource):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_links(cls, resource_data):
        pass

    @classmethod
    def get_data_resource_info(cls):
        return 'aaaaF21E6156', 'users'

    @classmethod
    def get_all_user_data(cls):
        res = RDBService.get_full_table("UsersInfo", "UsersInfo")
        return res