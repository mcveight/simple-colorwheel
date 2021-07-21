'''
Init module to start up the software

constant declarations and initializers will be defined
here

'''


from controller import controller


# CONSTANT DECLARATIONS
TITLE = "Simple colorwheel?"
GEOMETRY = "200x420"

swc = controller(TITLE, GEOMETRY)
