import logging
logging.basicConfig(filename ="abs.log",level=logging.DEBUG ,format="%(levelname)s %(asctime)s %(message)s")

class ineuron : #abstarct class

    def jobs(self):
        pass


    def courses(self):
        pass


    def blogs(self):
        pass


class job(ineuron):

    def jobs(self):
        try:
            logging.info("this functions gives jobs description")
        except Exception as e:
            logging.error(e)

class course(ineuron):

    def courses(self):
        try:
            logging.info("this function gives course information")
        except Exception as e:
            logging.error(e)

class blog(ineuron):

    def blogs(self):
        try:
            logging.info("this functions provides blogs ")
        except Exception as e:
            logging.error(e)

j = job()
logging.info(j.jobs())

c = course()
logging.info(c.jobs())

b = blog()
logging.info(b.blogs())
