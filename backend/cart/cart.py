from courses.models import Courses
from decimal import Decimal
class Cart():
    def __init__(self,request):
        self.session = request.session
        
        #Get the current session key
        cart = self.session.get('session_key')
        
        #if user is new, create one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
            
        
        #Cart is avalable on all pages
        self.cart = cart
        
    def add(self, course, quantity=1):
        course_id = str(course.id)
        
        if course_id in self.cart:
            self.cart[course_id]['quantity'] += quantity
        else:
            self.cart[course_id] = {'price': str(course.price), 'quantity': quantity}
            
        self.session.modified = True
        
    def __len__(self):
        return sum(item.get('quantity', 1) for item in self.cart.values())

    
    def get_courses(self):
        #get all ids from cart
        course_ids = self.cart.keys()
        #use ids to look up course
        courses = Courses.objects.filter(id__in=course_ids)
        # Add individual totals to each course
        for course in courses:
            course_id = str(course.id)
            quantity = self.cart[course_id].get('quantity', 1)
            if course.is_sale:
                course.individual_total = course.sale_price * quantity
            else:
                course.individual_total = course.price * quantity

        return courses
    
    def delete(self, course):
        course_id = str(course)
        # Delete from dictionary/cart
        if course_id in self.cart:
            del self.cart[course_id]
            
        self.session.modified = True
    
    def cart_total(self):
        # get course_id
        course_ids = self.cart.keys()
        #use ids to look up course
        courses = Courses.objects.filter(id__in=course_ids)
        # init total = 0
        total = Decimal('0.00')
        for key, value in self.cart.items():
            key = int(key)
            quantity = value.get('quantity', 1)
            for course in courses:
                if course.id == key:
                    if course.is_sale:
                        total += course.sale_price * quantity
                    else:
                        total += course.price * quantity
        return total