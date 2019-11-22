                # scope: What variables do I have access to?
def outer():
    x = "local"
    
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    
    inner()
    print("outer:", x)
outer()

#security login create -user-or-group-name cvadmin_ontap -application ssh -authentication-method password -role backup -is-ns-switch-group no -second-authentication-method none -vserver in-nfspoc-na1 -comment "commvault
#backup user account"