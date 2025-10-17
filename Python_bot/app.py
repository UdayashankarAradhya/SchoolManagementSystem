from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
app.secret_key = 'your_secret_key'

students = []

# Preload with 50 dummy student records
for i in range(1, 51):
    students.append({'name': f'Nikhil', 'roll': str(100 + i), 'course': 'ECE'})

@app.route('/sms', methods=['POST'])
def sms_reply():
    incoming_msg = request.values.get('Body', '').strip()
    resp = MessagingResponse()
    msg = resp.message()

    if 'state' not in session:
        session['state'] = None

    state = session['state']

    if incoming_msg.lower() == 'hi':
        msg.body("Hey there! 👋 Welcome to the School Management System bot. Type 'menu' to begin.")
        session['state'] = None
        return str(resp)

    if incoming_msg.lower() == 'menu':
        session['state'] = None
        msg.body("""📋 Menu:
1. Add Student
2. View Student
3. Delete Student
4. Find by Roll
5. Find by Name
6. List by Course
7. Count of Students
8. Update Student

Type the option number:""")
        return str(resp)

    # Add student
    if state == 'adding':
        parts = incoming_msg.split()
        if len(parts) == 3:
            name, roll, course = parts
            students.append({'name': name, 'roll': roll, 'course': course})
            msg.body("✅ Student added successfully.")
        else:
            msg.body("❌ Invalid format. Use: name roll course")
        session['state'] = None
        return str(resp)

    if incoming_msg == '1':
        session['state'] = 'adding'
        msg.body("To add student, send details in format:\nname roll course\nExample: uday 177 ECE")
        return str(resp)

    # View student
    if state == 'viewing':
        roll = incoming_msg
        for s in students:
            if s['roll'] == roll:
                msg.body(f"👤 Name: {s['name']}\n🆔 Roll: {s['roll']}\n📚 Course: {s['course']}")
                break
        else:
            msg.body("❌ Student not found.")
        session['state'] = None
        return str(resp)

    if incoming_msg == '2':
        session['state'] = 'viewing'
        msg.body("Enter Roll to View")
        return str(resp)

    # Delete student
    if state == 'deleting':
        roll = incoming_msg
        for s in students:
            if s['roll'] == roll:
                students.remove(s)
                msg.body("🗑️ Student deleted.")
                break
        else:
            msg.body("❌ Student not found.")
        session['state'] = None
        return str(resp)

    if incoming_msg == '3':
        session['state'] = 'deleting'
        msg.body("Enter Roll to Delete")
        return str(resp)

    # Find by roll
    if state == 'finding_by_roll':
        roll = incoming_msg
        for s in students:
            if s['roll'] == roll:
                msg.body(f"👤 Name: {s['name']}\n🆔 Roll: {s['roll']}\n📚 Course: {s['course']}")
                break
        else:
            msg.body("❌ Student not found.")
        session['state'] = None
        return str(resp)

    if incoming_msg == '4':
        session['state'] = 'finding_by_roll'
        msg.body("Enter Roll to Find")
        return str(resp)

    # Find by name
    if state == 'finding_by_name':
        name = incoming_msg.lower()
        found = [s for s in students if s['name'].lower() == name]
        if found:
            result = "\n\n".join([f"👤 {s['name']} | 🆔 {s['roll']} | 📚 {s['course']}" for s in found])
            msg.body(result)
        else:
            msg.body("❌ Student not found.")
        session['state'] = None
        return str(resp)

    if incoming_msg == '5':
        session['state'] = 'finding_by_name'
        msg.body("Enter Name to Find")
        return str(resp)

    # List by course
    if state == 'listing_by_course':
        course = incoming_msg.upper()
        found = [s for s in students if s['course'].upper() == course]
        if found:
            result = "\n\n".join([f"👤 {s['name']} | 🆔 {s['roll']} | 📚 {s['course']}" for s in found])
            msg.body(result)
        else:
            msg.body("❌ No students found in that course.")
        session['state'] = None
        return str(resp)

    if incoming_msg == '6':
        session['state'] = 'listing_by_course'
        msg.body("Enter course name (e.g., ECE, CSE):")
        return str(resp)

    # Count
    if incoming_msg == '7':
        msg.body(f"📊 Total Students: {len(students)}")
        return str(resp)

    # Update student
    if state == 'updating':
        parts = incoming_msg.split()
        if len(parts) == 3:
            name, roll, course = parts
            for s in students:
                if s['roll'] == roll:
                    s['name'] = name
                    s['course'] = course
                    msg.body("♻️ Student updated.")
                    break
            else:
                msg.body("❌ Student not found.")
        else:
            msg.body("❌ Invalid format. Use: name roll course")
        session['state'] = None
        return str(resp)

    if incoming_msg == '8':
        session['state'] = 'updating'
        msg.body("Send updated details as: name roll course")
        return str(resp)

    msg.body("❓ Sorry, I didn't understand that. Type 'menu' to see options.")
    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)
