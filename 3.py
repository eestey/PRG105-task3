print "[======================]"
print "   1. Returning Customer"
print "   2. New Customer"
print "   3. Guest"
print "[======================]\n"
choice = 0


def get_customer():
    customer_id = raw_input('Please enter your user ID:  \n')
    print '\n'
    return customer_id


def find_customer(customer_id):
    try:
        with open('CustomerList.txt', 'r+') as lists:
            customer_list = lists.readlines()
            for line in customer_list:
                record = line.split(',')
                if customer_id == record[0]:
                    return record
        return 'none'
    except IOError:
        print('File not found')


def confirm():
    c = raw_input("Is this the correct info?: \nY/N\n").capitalize()

    if c == 'N':
        print "Please re-enter correct info. \n"
        returning()

    else:
        print 'Thank You'


def returning():
    customer = get_customer()
    records = find_customer(customer)
    if records == 'none':
        print "Customer ID not found"
        returning()

    else:
        for items in records:
            print items

        confirm()
    return


while choice < 1 or choice > 3:
    choice = (int(raw_input("Please select customer type\n Enter a value between 1 and 3: \n")))
    if choice == 1:
        returning()
    elif choice == 2:
        print "New Customer \n"
    elif choice == 3:
        print "Hello Guest."
    else:
        print ValueError("Please choose 1 for Returning Customer, 2 for New Customer, or 3 for Guest.")
