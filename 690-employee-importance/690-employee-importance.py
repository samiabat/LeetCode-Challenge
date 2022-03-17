class Solution:
    
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        """
            DFS subordinates
            
            map all employee ids to indexes
        """
        
        mappings = dict()
        for index, employee in enumerate(employees):
            mappings[employee.id] = index            
        def helper(id):
            total_importance = employees[mappings[id]].importance
            for subordinate in employees[mappings[id]].subordinates:
                total_importance += helper(subordinate)
            return total_importance
        return helper(id)