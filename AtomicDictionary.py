def AtomicDictionary():
    element={"H":"Hydrogen"}
    print(element)
    unikey=input("enter the element symbol")
    unival=input("enter the element name")
    element.update({unikey:unival})
    print(element)
    unikey=input("enter the duplicate element symbol")
    unival=input("enter the duplicate element name")
    element.update({unikey:unival})
    print(element)
    search =input("enter element to be searched")
    if search in element.values():
        print("element found")
    else:
        print("element not found")
AtomicDictionary()