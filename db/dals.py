

class DataDAL:
    def __init__(self, db_session):
        self.db_session = db_session

    async def crete_phone(self, phone: str, address: str):
        return self.db_session.set(phone, address)

    async def get_address(self, phone):
        return self.db_session.get(phone)

    async def update_address(self, phone, address):
        return self.db_session.set(phone, address)

    async def delete_address(self, phone):
        return self.db_session.delete(phone)
