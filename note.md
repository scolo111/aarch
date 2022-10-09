## class nested_cond (aka. nc)
### var: name
it could be if, case 
### var: cond_list
```
Ex.
if <con1> then
else if <cond2> then
else if <cond3>

cond_list = [cond1,cond2,cond3]
```
```
Ex.
case <con1> of
    when <cond2>:
    when <cond3>:

cond_list = [cond1,cond2,cond3]
```
## nested usage 
1. case - case - if  
2. case - if
3. case - case 
4. if - if  

[
    {
        type:'case'
        cond: 'op1:op2'= '000 011'
        value: [
            {
                type: 'if'
                cond: '!HaveUAOExt()'
                value: UNDEFINED
            }
        ]
    }
    ...
    {
        type:'case'
        cond: 'op1:op2'= '011 011'
        value: [
            {
                type: 'case'
                cond: 'CRm == '001x'
                value: [
                    {
                        type: 'if'
                        cond: '!HaveSME()'
                        value: UNDEFINED
                    }
                    ...
                ]
            }
            ...
            {
                type: 'case'
                cond: '!( || || || )'
                value: [
                    UNDEFINED
                ]
            }
        ]
        
    }

]

nc1.cond_list = [cond1, {when: [cond1,]}, !()]




