from flet import *
# IMPORT YOU CREATE TABLE 
from myaction import create_table
from datatable import mytable,tb,calldb
import sqlite3
conn = sqlite3.connect("db/dbone.db",check_same_thread=False)

def main(page:Page):

	# AND RUN SCRIPT FOR CREATE TABLE WHEN FLET FIRST RUN
	create_table()

	page.scroll = "auto"

	def showInput(e):
		inputcon.offset = transform.Offset(0,0)
		page.update()

	def hidecon(e):
		inputcon.offset = transform.Offset(2,0)
		page.update()

	def savedata(e):
		try:
			# INPUT TO DATABASE
			c = conn.cursor()
			c.execute("INSERT INTO users (name,age,contact,email,address,gender) VALUES(?,?,?,?,?,?)",(name.value,age.value,contact.value,email.value,address.value,gender.value))
			conn.commit()
			print("success")

			# AND SLIDE RIGHT AGAIN IF FINAL INPUT SUUCESS
			inputcon.offset = transform.Offset(2,0)

			# ADD SNACKBAR IF SUCCESS INPUT TO DATABASE

			page.snack_bar = SnackBar(
				Text("success INPUT"),
				bgcolor="green"
				)

			page.snack_bar.open = True

			# REFRESH TABLE
			tb.rows.clear()
			calldb()
			tb.update()
			page.update()


		except Exception as e:
			print(e)

	# CREATE FIELD FOR INPUT

	name = TextField(label="name")
	age = TextField(label="age")
	contact = TextField(label="contact")
	email = TextField(label="email")
	address = TextField(label="address")
	gender = RadioGroup(content=Column([
		Radio(value="man",label="man"),
		Radio(value="woman",label="woman")

		]))

	# CREATE MODAL INPUT FOR ADD NEW DATA 
	inputcon = Card(
		# ADD SLIDE LEFT EFFECT
		offset = transform.Offset(2,0),
		animate_offset = animation.Animation(600,curve="easeIn"),
		elevation=30,
		content=Container(
			content=Column([
				Row([
				Text("Add new data",size=20,weight="bold"),
				IconButton(icon="close",icon_size=30,
				on_click=hidecon
					),
					]),
				name,
				age,
				contact,
				email,
				gender,
				address,
				FilledButton("save data",
				on_click=savedata
					)

			])

		)

		)


	page.add(
	Column([
		Text("SCHOLL APP",size=30,weight="bold"),
		ElevatedButton("add new data",
		on_click=showInput
		),
		mytable,
		# AND DIALOG FOR ADD DATA
		inputcon 


		# NOTICE IF YOU ERROR
		# DISABLE import Datatable like this
		])

		)

flet.app(target=main)
