add Entity(db.Model):
	Room
		id
		name
		capacity
	User
		id
		firstname
		lastname
        age
    Lesson
		id
		name
		teacher (User.id)
	Group
		id
		name
		members (list(user.id))
	Sсheduler
		id
		room (room.id)
		lesson (lesson.id)
		group (group.id)
		date
		para (1..7 int)
    
* створитии відповідні сутності
* створитии форми і темплейти для можливості додавання і тедагування відповідних сутностейй
* на головні сторінці створити меню з можливіть переходу на сторінки для перегляду/редагування/видалення кожної сутності 
* також на головній сторінці відображати пари які мають відбуватися в поточний день