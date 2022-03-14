import SecretsProxy as sp
import time 
import EnvironProxy as ep

class TermKeeper:
    term_check_time = 0
    term_check_duration = int(ep.get_env('TERM_CHECK_DURATION'))
    search_term = 'asd'
   
    def get_search_terms(self):
        now = time.time()

        if now > (self.term_check_time + self.term_check_duration):
            self.search_term = sp.get_search_terms()
            self.term_check_time = now

        
        return self.search_term[:]