#!/usr/bin/env python
import re, sys

examples = """
fix: navbar not responsive on mobile
test: prepared test cases for user authentication
chore: moved to semantic versioning
feat(auth): added social login using twitter
"""

types = """
\033[41mnew\033[m: Newly created
\033[41mdocs\033[m: Documentation only changes
\033[42mfeat\033[m: A new feature
\033[42mfix\033[m: A bug fix
\033[43mperf\033[m: A code change that improves performance
\033[43mrefactor\033[m: A code change that neither fixes a bug nor adds a feature
\033[44mstyle\033[m: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
\033[44mtest\033[m: Adding missing tests or correcting existing tests
\033[45mchore\033[m: Changes to the build process or auxiliary tools
\033[45mrevert\033[m: Roll back the previous version
\033[46mmerge\033[m: Code merge
\033[46msync\033[m: Synchronize bugs in the master or branch
"""

def main():
	pattern = r'(new|docs|feat|fix|perf|refactor|style|test|chore|revert|merge|sync)(\([\w\-]+\))?:.*'
	filename = sys.argv[1]
	try:
		ss = open(filename, 'r', encoding='gbk').read()
	except:
		ss = open(filename, 'r', encoding='utf-8').read()
	m = re.match(pattern, ss)
	if m == None:
		print("\nCOMMIT FAILED!")
		print("\nPlease enter commit message in the conventional format and try to commit again. Examples:")
		print("\n" + examples)
		print("\nCHECK COMMIT CONVENTIONS BELOW!\n" + types)
		sys.exit(1)
	else:
		commitPrefix = ss.split(':')[0]
		commitPostfix = ss.split(':', 1)[1]
		if '(' in commitPrefix:
			newCommit = open(filename, 'w')
			newCommit.write(commitPrefix + ": " + commitPostfix)
		else:
			newCommit = open(filename, 'w')
			newCommit.write(commitPrefix + ": " + commitPostfix)

if __name__ == "__main__":
	main()
