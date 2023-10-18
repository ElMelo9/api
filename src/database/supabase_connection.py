import supabase

# Configura las credenciales de tu proyecto de Supabase
SUPABASE_URL = 'https://lueghozveikcdzjwweag.supabase.co'
SUPABASE_API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imx1ZWdob3p2ZWlrY2R6and3ZWFnIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTc1OTc4NDIsImV4cCI6MjAxMzE3Mzg0Mn0.QstyUrwmGBzpZnta7pqnxJgcJSDIIwawS-5isgsnIpw'

# Crea una instancia de Supabase
supabase_client = supabase.create_client(SUPABASE_URL, SUPABASE_API_KEY)

