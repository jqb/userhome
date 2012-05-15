userhome
========

Simple os-independent tool for getting user home directory path.
Currently works for posix systems and windows.


usage
-----

Assuming, you're login on the system as "jacob", usage looks like this::


   # On windows
   >>> import userhome
   >>> userhome.path() == 'C:\\Users\\jacob'
   >>> userhome.path(".templates") == 'C:\\Users\\jacob\\.templates'
   >>> userhome.path(".templates", "django") == 'C:\\Users\\jacob\\.templates\\django'

   # On linux and other posix systems
   >>> import userhome
   >>> userhome.path() == '/home/jacob/'
   >>> userhome.path(".templates") == '/home/jacob/.templates'
   >>> userhome.path(".templates", "django") == '/home/jacob/.templates/django'
