import hudson.model.*
import hudson.EnvVars
import groovy.json.JsonSlurperClassic
import groovy.json.JsonBuilder
import groovy.json.JsonOutput
import java.net.URL

// loading and running jenkins tasks 
workspace = pwd()
ok = '\u2705'
no = '\u274C'

stage 'Init Working Env'
node() {
	echo "${ok} Check Workspace: ${workspace}/"
	echo "${ok} Check Ansible Availability"
	sh 'which ansible'
	echo "${ok} Check Ansible Version"
	sh 'ansible --version'
	echo "${no} Something's wrong..."
	echo '$&@*&%#)(*#@(*_)*&%#*^@&$)*'
  sh "ls -ltrh ${workspace}/bin/"
}

stage "Deploy Application"
node() {
	sh "cd ${workspace}/bin/;sudo ansible-playbook -i hosts auto-rest.yml"
}

stage "Task Finalized"
node() {
	echo "Tasks finalized"
}
