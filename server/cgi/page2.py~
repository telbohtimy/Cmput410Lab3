#!/usr/bin/env python

import cgi
form =cgi.FieldStorage()
val1=form.getvalue("first")
val2=form.getvalue("family")
print """Content-type:text/html

<form method="post" action="page1.py">
<textarea name="birthdate" cols="40" rows="1">
Birthdate
</textarea>
<textarea name="hobby" cols="40" rows="1">
Hobby
</textarea>
<br/>
<input type="submit" value="Submit">
</form>"""

print val1,val2
