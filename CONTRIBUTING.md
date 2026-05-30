# Contributing Guidelines

:heavy_check_mark::tada: Let's make code better together - Thanks for taking the time to contribute! :tada::heavy_check_mark:

The following is a set of guidelines for contributing to *0x0I Ansible roles*, which are hosted under the [0x0I](https://github.com/0x0I?tab=repositories) developer account on GitHub. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

For general information and guidelines for contributing to these roles and the Ansible community, see the [community page](https://docs.ansible.com/ansible/latest/community/).

**Table of Contents**
  - [Pull Requests](#pull-requests)
      - [CI Pipeline](#ci-pipeline)
  - [Issues](#issues)
      - [Issue Types](#issue-types)
  - [Workflow and backlog](#workflow-and-backlog)
  - [Code of Conduct](#code-of-conduct)

## Pull Requests

All [PRs](https://github.com/0x0I/ansible-role-systemd/pulls) are welcome! :+1: The following guidelines and CI pipeline are provided for validating role functionality and avoiding regressions for each submitted request:

Install test and lint dependencies from the repo root:

```bash
python -m pip install -r tests/requirements.txt
```

#### CI Pipeline

| Test | Description | Dependencies | Validation Command |
| --- | --- | --- | --- |
| :zap: `yamllint` | Validates `yaml` adheres to coding standards and best practices as [configured](https://github.com/O1ahmad/ansible-role-systemd/blob/master/tests/yaml-lint.yml). | [yamllint](https://yamllint.readthedocs.io/en/stable/) | `yamllint --config-file ./tests/yaml-lint.yml .` |
| :zap: `ansible-lint` | Validates Ansible module and construct usage as [configured](https://github.com/O1ahmad/ansible-role-systemd/blob/master/tests/ansible-lint.yml). | [ansible-lint](https://docs.ansible.com/ansible-lint/) | `ansible-lint --config-file ./tests/ansible-lint.yml .` |
| :wrench: `molecule` | Integration tests for config, launch, and uninstall scenarios using Docker. Shared scenario settings live in [tests/molecule/base.yml](https://github.com/O1ahmad/ansible-role-systemd/blob/master/tests/molecule/base.yml). | [Molecule](https://ansible.readthedocs.io/projects/molecule/) + [molecule-docker](https://github.com/ansible-community/molecule-plugins) | `cd tests && molecule --base-config molecule/base.yml test -s <scenario>` |
| :traffic_light: `Continuous Integration (CI)` | GitHub Actions runs lint and Molecule on each push and pull request. Requests should not be merged unless all jobs pass or the community approves otherwise. | *N/A* | *see* [.github/workflows/CI.yaml](https://github.com/O1ahmad/ansible-role-systemd/blob/master/.github/workflows/CI.yaml) |

Example Molecule commands:

```bash
cd tests && molecule --base-config molecule/base.yml test -s config
cd tests && molecule --base-config molecule/base.yml test -s launch
cd tests && molecule --base-config molecule/base.yml test -s uninstall
```

## Issues

New GitHub issues can be [opened](https://github.com/0x0I/ansible-role-systemd/issues/new) and [tracked](https://github.com/0x0I/ansible-role-systemd/issues) in a similar fashion as with most Github repositories by making use of the standard Github issue management facilities.

Reference the following issue reporting guide for more details:

#### Issue Types

| Issue Type | Description |
| --- | --- |
| :arrow_up: `:enhancement:` | Feature requests. |
| :bug: `:bug:` | Confirmed bugs or reports that are very likely to be bugs. |
| :question: `:question:` | Questions more than bug reports or feature requests (e.g. how do I do X). |
| :eyeglasses: :heartpulse:`:feedback:` | General feedback more than bug reports or feature requests. |

## Workflow and backlog

Reference this repository's [wiki](https://github.com/0x0I/ansible-role-systemd/wiki) to visualize the project roadmap, workflow and backlog to stay up to speed with development  plans and work in progress.

## Code of Conduct

See the [Ansible Code of Conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html).
