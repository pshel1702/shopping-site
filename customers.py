"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""
    
    def __init__(self, 
                 firstname, 
                 lastname, 
                 email, 
                 password,
                 ):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
    
    def __repr__(self):
        """Convenience method to show information in terminal."""
        
        return "<Customer: {} {}, {}>".format(self.firstname,self.lastname,self.email)

def read_customer_info_from_file(filepath):
    """Read customer info from file path and populate dictionary."""

    email_lookup = {}

    with open(filepath) as file:
        for line in file:
            (firstname,
            lastname,
            email,
            password) = line.strip().split("|")
            email_lookup[email] = Customer(firstname,lastname,email,hash(password))
    
    return email_lookup

def get_by_email(email_id):
    """Return customer info based on email lookup.
       If you call this function, you should get back a list like the one below.
           
       >>> get_by_email('jane@jane.com').email
       'jane@jane.com'
    """
    return email_lookup[email_id]

email_lookup = read_customer_info_from_file("customers.txt")
