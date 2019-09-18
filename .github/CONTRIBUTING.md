# How to Contribute

Coderplex web application comprises of two repositories :

* [OpenRank-Frontend](https://github.com/coderplex/openrank-frontend) : Frontend of the application

* [OpenRank-Backend](https://github.com/coderplex/openrank-backend) : Backend of the application, where API calls are made.

* [OpenRank-Execution](https://github.com/coderplex/openrank-backend) : Backend of the application, where code execution and server-side testing happens.

## Table Of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Code of Conduct](#code-of-conduct)
- [Open Development](#open-development)
- [Branching Model](#branching-model)
- [Development Workflow](#development-workflow)
  - [Work on Issues](#work-on-issues)
  - [Proposing a Change](#proposing-a-change)
  - [Prerequisites](#prerequisites)
  - [Sending a Pull Request](#sending-a-pull-request)
    - [Running Locally](#running-locally)
    - [Before submitting](#before-submitting)
    - [Add yourself as a contributor](#add-yourself-as-a-contributor)
    - [Submitting PullRequest](#submitting-pullrequest)
    - [After submitting](#after-submitting)
      - [Received a review request](#received-a-review-request)
  - [How to get in touch](#how-to-get-in-touch)
- [Appendix](#appendix)
  - [Node Version Manager](#node-version-manager)
    - [nvm for Linux & macOS](#nvm-for-linux--macos)
    - [nvm-windows for Windows](#nvm-windows-for-windows)
  - [Local host occupied](#local-host-occupied)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Code of Conduct

Coderplex has adopted [Contributor Covenant](/.github/CODE_OF_CONDUCT.md) that we expect project participants to adhere to.

## Open Development

All work related to the application takes place on Github itself. We use [Issues](https://github.com/coderplex/openrank-backend/issues) to track bugs, discuss ideas and to engage open source contributors. [Projects](https://github.com/coderplex/openrank-backend/projects) are used to keep track of everything and is our project management tool. We maintain [Wiki](https://github.com/coderplex/openrank-backend/wiki) for structuring our long term thoughts. Both core team members and contributors sends a pull request which goes through the same review process. Whole process is as transparent as it can be and we strive to keep it that way.

## Branching Model

The `master` branch of coderplex is relatively stable branch which we update for every release. We also have auto deployment in place for that particular branch i.e any changes in that branch gets reflected in [https://openrank.coderplex.org](https://openrank.coderplex.org). It is highly recommended for both maintainers and contributors to raise a pull request to `develop` branch. Before every release we throughly test develop branch and merge into master.

![Imgur](https://i.imgur.com/KPO2dLul.png)

_A pull request to any other branch may most likely be closed by our bots_.

## Development Workflow

We welcome pull requests from beginners and seasoned javaScript developers alike!

### Work on Issues

1. Find an issue that needs assistance by searching for the [open issues](https://github.com/coderplex/openrank-backend/labels/help-wanted).
1. If you decide to fix an issue, please be sure to check the comment thread in case somebody is already working on a fix. If nobody is working on it at the moment, please leave a comment stating that you intend to work on it so other people don’t accidentally duplicate your effort.
1. If somebody claims an issue but doesn’t follow up for more than a weeks, it’s fine to take over it but you should still leave a comment.

### Proposing a Change

1. Open a new issue if you would like report a bug or suggest improvements.
1. Please wait for core team members to comment on the thread. This lets us reach an agreement on your proposal before you put significant effort into it.

### Prerequisites

1. [NodeJS](https://nodejs.org/)

   * Minimum version v8.0.0+

   ```bash
   # To check node version
   node -v
   ```

   Any lower version than mentioned above may results in this [error](https://github.com/coderplex/coderplex/issues/100).

   > If you face problem updating your node then you might need a Node version manager tool. [Follow here](#node-version-manager)

1. [Git](https://git-scm.com/download/linux) (Familiarity with git is mandatory).

### Sending a Pull Request

*Working on your first Pull Request? You can learn how from this *free* series [How to Contribute to an Open Source Project on GitHub](https://egghead.io/series/how-to-contribute-to-an-open-source-project-on-github)*

#### Running Locally

1. Fork the [repository](https://github.com/coderplex/coderplex).
1. Then clone your forked repository
   ```bash
    git clone <your forked repository url>
   ```
1. Move to the repository root folder
   ```bash
    cd openrank-backend
   ```
1. Install dependencies
   ```bash
    npm install
   ```
1. Create a `.env` file and values from `.env.example`. Change the values according to the environment that you're using to run the project. Make sure that you have database server running at port that you specified in the `.env` file.
    > **Note**: You need to create a database manually because sequelize doesn't support creation of users and databases.
1. Migrate the models to database.
   ```bash
    npm run migrate
   ```
1. Start the development server
   ```bash
    //for development server using nodemon
    npm run start:dev
    //for running server using node
    npm run start
   ```
   App now opens at `localhost:8000` in your default browser. If it doesn't, once you see a message on console saying the development server is hosted at above mentioned address. Please visit [localhost:8000](http://localhost:8000) in the browser of your choice.
   > You may get this [error](#local-host-occupied) if any other app is already running the above port.

#### Before submitting

1. From your fork, create a [branch](https://help.github.com/articles/creating-and-deleting-branches-within-your-repository/) and name it. eg. `typo-in-readme` or `issue-9-fix` or `issue-12-feature-addition`
1. If you’ve fixed a bug or added code that should be tested, add tests!
1. Ensure that all test pass
   ```bash
    npm run test
   ```
1. Run code formatters
   ```bash
    npm run lint
   ```
1. Add and commit your code. Please give meaning full commit messages.

#### Add yourself as a contributor

This project follows the [all-contributors](https://github.com/kentcdodds/all-contributors) specification. Contributions of any kind welcome!

To add yourself to the table of contributors on the `README.md`, please use the automated script as part of your PR:

```bash
yarn run add-contributor
```

Follow the prompt and commit `.all-contributorsrc` and `README.md` in the PR.

#### Submitting PullRequest

1. Pull latest code from [upstream repository's](https://help.github.com/articles/merging-an-upstream-repository-into-your-fork/)`develop`, if in case anything new were merged while you were working on your fork.
1. Push the code to your fork.
1. Raise the pull request from your created branch to `develop` branch of coderplex. [why develop instead of master branch?](https://www.atlassian.com/git/tutorials/comparing-workflows)
1. Take some time to give a brief description of the work you have done.

#### After submitting

1. Wait for all checks to pass in below section.
1. Your changes are deployed with a unique link `https://deploy-preview-xx--coderplex.netlify.com`.

   _`- xx` is your pull request number._

1. The core team will review your pull request and either merge it, request changes to it, or close it with an explanation.

##### Received a review request

* Work on the requested changes
* Push the changes as you did earlier, the pull request will automatically catch those and update itself.

### How to get in touch

* OpenRank [Discord Channel](https://discord.gg/ppXaS3)
<!-- * Tweet core team members :
  * Vinay Puppal [@VinayPuppal](https://twitter.com/vinaypuppal)
  * Md-ZubairAhmed [@Md_ZubairAhmed](https://twitter.com/Md_ZubairAhmed) -->

## Appendix

### Node Version Manager

#### [nvm](https://github.com/creationix/nvm) for Linux & macOS

```bash
# Installation
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.6/install.sh | bash

# Install latest node lts
nvm install --lts

# Use installed version
nvm use --lts

# Run the app in the same terminal session
```

_Make sure you have [curl](https://curl.haxx.se/) installed_

#### [nvm-windows](https://github.com/coreybutler/nvm-windows) for Windows

It comes with an [installer](https://github.com/coreybutler/nvm-windows#installation--upgrades).

```bash
# Install particular version
nvm install 8.9.1

# Use installed version
nvm use 8.9.1
```

Still facing problem this [article](https://medium.com/appseed-io/how-to-run-multiple-versions-of-node-js-with-nvm-for-windows-ffbe5c7a2b47) from [@skounis](https://twitter.com/skounis) explain in details.

### Local host occupied

```js
Error: listen EADDRINUSE :::8000
    at Object._errnoException (util.js:1024:11)
    at _exceptionWithHostPort (util.js:1046:20)
    at Server.setupListenHandle [as _listen2] (net.js:1351:14)
    at listenInCluster (net.js:1392:12)
    at Server.listen (net.js:1476:7)
    at app.prepare.then (/home/m-zubairahmed/github/official/openrank-backend/server.js:26:6)
    at <anonymous>
    at process._tickCallback (internal/process/next_tick.js:188:7)
error Command failed with exit code 1.
```

If you get this error while running `rpm run start:dev` then probably another app is occupying `localhost:8000`. You may want to close that and run the command again.
