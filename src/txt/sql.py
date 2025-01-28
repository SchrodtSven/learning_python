# Small collection of classes for building sql stuff dynamically | sql.py
# 
# 
# SUBJECT: learning baby python
# AUTHOR Sven Schrodt <sven@schrodt.club>


class QueryBuilder:
    """ (S)Q(L)uery building class
        - method name starting with '_', avoiding name conflicts (from <-> from / --> _from())
        
        - TODO/FIXME -> clauses etc. wanna be instances themselves ;-)

    Returns:
        _type_: _description_
    """
    sql = ''
    table = None
    where = None
    
    def __init__(self, table=''):
        if table != '':
            self._from(table)
        else:
            self.table = None
            
    def _select(self, what='*'):
        if isinstance(what, list):
            what = ', '.join(what)
        self.sql += 'SELECT ' + what
        return self
    
    def _from(self, t_name):
        self.table = t_name
        self.sql += ' FROM ' + t_name
        return self
    
    def _where(self, clause):
        
        self.where = clause
        self.sql += ' WHERE ' + clause
        return self
    
    def __str__(self):
        return self.sql
    
qb = QueryBuilder()
#qb._select(['id', 'first', 'email'])._from('my_clients')
qb._select(['id'])._from('my_clients')._where('zip BETWEEN 47000 AND 51000')

print(qb)