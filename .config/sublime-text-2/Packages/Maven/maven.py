import sublime, sublime_plugin

class MavenGoalsCommand(sublime_plugin.WindowCommand):
	wrkDir = None
	cmd = None

	def run(self,working_dir,cmd):
		self.cmd = [cmd]
		self.wrkDir = working_dir
		#print self.wrkDir
		self.window.show_input_panel("mvn",'clean test',self.on_done,None,None)

	def on_done(self, text):
		self.cmd += [u'-B']
		self.cmd += text.split(' ')
		#print cmd
		self.window.run_command("exec",{"cmd":self.cmd, 'working_dir':self.wrkDir})
