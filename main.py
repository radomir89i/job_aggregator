from tornado.web import Application, RequestHandler
import tornado.ioloop
from workersmgmt import Worker

class basicRequestHandler(RequestHandler):
    def get(self):
        self.write('Hi wrld!')


class getjobsRequestHandler(RequestHandler):
    def get(self):
        self.render('getjobs.html')


class queryStringRequestHandler(RequestHandler):
    def get(self):
        worker_id = int(self.get_argument('workerId'))
        if worker_id % 2 == 0:
            self.write('worker is working')
        else:
            self.write('worker fucked up')


class resourceRequestHandler(RequestHandler):
    def get(self, id):
        self.write('tweet number' + id)


class runJobHandler(RequestHandler):
    def post(self, source_type, vacancy_name, from_date, task_type):
        worker = Worker(source_type, vacancy_name, from_date, task_type)
        worker.run()


if __name__ == '__main__':
    app = Application([
        (r'/', basicRequestHandler),
        (r'/GET_JOBS', getjobsRequestHandler),
        (r'/workerStatus', queryStringRequestHandler),
        (r'/tweet/([0-9]+)', resourceRequestHandler),
        (r'/RUN_JOB', runJobHandler),
    ])

    app.listen(8899)
    print('Im listening on port 8899')
    tornado.ioloop.IOLoop.current().start()