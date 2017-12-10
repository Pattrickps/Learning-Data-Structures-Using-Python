#heap-sort

class Heap:
    def __init__(self):
        self.l=[0]
        self.currentsize=0

    def compare_with_root(self,index):
        
            
        root=index//2
        if self.l[index]>self.l[root]:
            return True
        else:
            return False
                
           
                
            

    def moveup(self,index):
        while(1):
            if index==1:
                break
            root=index//2
            if self.compare_with_root(index):
                temp=self.l[root]
                self.l[root]=self.l[index]
                self.l[index]=temp
                index=root
            else:
                break

    def insert(self,array):
        for i in array:
            self.l.append(i)
            self.currentsize+=1
            self.moveup(self.currentsize)
            
    def get_max_child(self,index):
        root=index
        left_child_index=2*root
        right_child_index=2*root + 1
        if left_child_index>self.currentsize:
            return None
        elif right_child_index>self.currentsize:
            return left_child_index
        else:
            return self.l.index(max(self.l[left_child_index],self.l[right_child_index]))

    def movedown(self,index):
        while(1):
            c_index=self.get_max_child(index)
            if c_index is not None and self.l[c_index] > self.l[index] :
                temp=self.l[c_index]
                self.l[c_index]=self.l[index]
                self.l[index]=temp
                index=c_index
            else:
                break
            
            
                
            


    def sort(self,max_heap_array):
        while(1):
            if self.currentsize==1:
                break
            #------------------swapping first with last
            first_element=self.l[1]
            last_element=self.l[self.currentsize]
            temp=first_element
            self.l[1]=last_element
            self.l[self.currentsize]=temp
            #--------------------------------
            self.currentsize-=1
            
            
            root_index=1
            print("swapped",self.l)
            self.movedown(root_index)
            print("heapified",self.l)
            print("\n")
        
array=[6,5,3,1,8,7,2,4]
obj=Heap()
obj.insert(array)
print (obj.l)
obj.sort(obj.l)
print(obj.l)
