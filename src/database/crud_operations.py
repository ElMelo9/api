from database.supabase_connection import supabase_client


class  Crud:

    #insert
    def create_role(self,data):
        response, error = supabase_client.table('roles').upsert(data).execute()
        if error:
            return error
        return response
    
    def create_user(self,data):
        response, error = supabase_client.table('usuarios').upsert(data).execute()
        if error:
            return error
        return response

    def create_document(self,data):
        response, error = supabase_client.table('tipo_documento').upsert(data).execute()
        if error:
            return error
        return response  
    
    def create_chatHistory(self,data):
        response, error = supabase_client.table('historial_chat').upsert(data).execute()
        if error:
            return error
        return response     
    
    def create_translations(self,data):
        response, error = supabase_client.table('traducciones').upsert(data).execute()
        if error:
            return error
        return response 
    
    def create_ContactUs(self,data):
        response, error = supabase_client.table('contactenos').upsert(data).execute()
        if error:
            return error
        return response 
    
    #select
    def get_roles(self):
        response= supabase_client.table('roles').select('*').execute()
        assert len(response.data) > 0

        data = response.data

        return data

    def get_tipoDoc(self):
        response= supabase_client.table('tipo_documento').select('*').execute()
        assert len(response.data) > 0

        data = response.data

        return data
    
    def get_users(self):
        response= supabase_client.table('usuarios').select('*').execute()
        assert len(response.data) > 0

        data = response.data

        return data   

    def get_chatHistory(self):
        response= supabase_client.table('historial_chat').select('*').execute()
        assert len(response.data) > 0

        data = response.data

        return data   

    def get_translations(self):
        response= supabase_client.table('traducciones').select('*').execute()
        assert len(response.data) > 0

        data = response.data

        return data  

    def get_ContactUs(self):
        response= supabase_client.table('contactenos').select('*').execute()
        assert len(response.data) > 0

        data = response.data

        return data  