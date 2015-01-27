#!/usr/bin/env python
import cgi
form =cgi.FieldStorage()
val1=form.getvalue("birthdate")
val2=form.getvalue("hobby")
print """Content-type:text/html

<form method="post" action="page2.py">
<textarea name="first" cols="40" rows="1">
First Name
</textarea>
<textarea name="family" cols="40" rows="1">
Family Name
</textarea>
<br/>
<input type="submit" value="Submit">
</form>"""

print val1,val2
