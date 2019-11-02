class NewNode:
    def __init__(self, root):
        self.val = root
        self.left = None
        self.right =None
        self.hd = 0
def topview(root):
    if root is None:
        return
    else:
        q=[]
        q.append(root)
        q.append(root.left)
        q.append(root.right)
        q.append(root.left.left)
        q.append(root.left.right)
        q.append(root.right.left)
        q.append(root.right.right)
        
        m ={}
        hd =0
        root.hd = hd
        hdv1 = []
        while len(q)>0:
             root = q[0]
             hd = root.hd
             a=[]
             if hd not in m:
                 r0 = {hd:[root.val]}
                 m.update(r0)
                 
             if (root.left):
                    root.left.hd = hd-1 
                    a.append(root.left.val)
                    r1={root.left.hd:a}
                    l = len(m)
                    
                    #m[root.left.hd]=root.left
                    for n in m:           
                            
                        if n == root.left.hd:
                            m[root.left.hd].append(root.left.val)  
                            #r1 ={root.left.hd:a.append(root.left.val)}
                        
                    x = m.get(root.left.hd)
                    if x is None:
                            m.update(r1)
                            
                    
                                                   
                    
             if (root.right):
                    root.right.hd = hd+1      
                    r2={root.right.hd:[root.right.val]}
                    for k in m:
                        if k == root.right.hd:
                            m[root.right.hd].append(root.right.val)
                    y = m.get(root.right.hd)
                    if y is None:
                            m.update(r2)    
                    #m.update(r2)
                    #m[root.right.hd]=root.right
             q.pop(0)

        for i in sorted (m):
            print(m[i])





root = NewNode(1)
root.left =NewNode(2)
root.right =NewNode(3)
root.left.left =NewNode(4)
root.left.right =NewNode(5)
root.right.left=NewNode(6)
root.right.right =NewNode(7)
topview(root)
