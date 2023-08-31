# file hadling class.....

# use your python file to create a table element of html file and open in web browser.
import webbrowser

Docs = open('table.html','w')
table_template ="""
<html lang ='en'>
<head>
<meta charset='utf-8'>
<meta http-equiv= 'X-UA compatible' content= 'IE=edge'>
<meta name='viewport' content='width=device-width'>
<title>Movies TimeTable</title>
</head>
<body>
<div id='wrapper' style='background-color: cyan;'>
<table border="1" cellspacing="5" cellpadding="20">
<caption>Movie Schedule</caption>
<thead>
<tr>
<th>Movie</th>
<th>Date</th>
<th>Time</th>
</tr>
</thead>
<tbody>
<tr>
<th>Hell'Boy</th>
<td>Saturday</td>
<td>6:00pm</td>
</tr>
<tr>
<th>Jagun Jagun</th>
<td>Sunday</td>
<td>6:00pm</td>
</tr>
</tbody>
</table>
</div>
</body>
</html>"""
Docs.write(table_template)
Docs.close()
webbrowser.open('table.html')