# Copyright 2025 Jiaqi Liu. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import re

from git import RemoteProgress
from git import Repo
from git.exc import GitCommandError
from tqdm import tqdm

FORKS = [
    {
        "fork": "git@github.com:QubitPi/leadership-blogs.git",
        "upstream": "git@github.com:saicaca/fuwari.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/shadowsocks.git",  # ✅
        "upstream": "git@github.com:shadowsocks/shadowsocks-org.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/wg-easy.git",
        "upstream": "git@github.com:wg-easy/wg-easy.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/mieru.git",
        "upstream": "git@github.com:enfein/mieru.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/Archive.org-Downloader.git",
        "upstream": "git@github.com:MiniGlome/Archive.org-Downloader.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/arrows.app.git",
        "upstream": "git@github.com:neo4j-labs/arrows.app.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/neo4j-browser.git",
        "upstream": "git@github.com:neo4j/neo4j-browser.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/ankidroiddocs.git",
        "upstream": "git@github.com:ankidroid/ankidroiddocs.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/lexitheras.git",
        "upstream": "git@github.com:conorreid/lexitheras.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/graphrag.git",
        "upstream": "git@github.com:microsoft/graphrag.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/leidenalg.git",
        "upstream": "git@github.com:vtraag/leidenalg.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/whisper.git",
        "upstream": "org-14957082@github.com:openai/whisper.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/mlflow.git",
        "upstream": "git@github.com:mlflow/mlflow.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/llama_index.git",
        "upstream": "git@github.com:run-llama/llama_index.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/ollama.git",
        "upstream": "git@github.com:ollama/ollama.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/openai-spinningup.git",
        "upstream": "org-14957082@github.com:openai/spinningup.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/scikit-learn.git",
        "upstream": "git@github.com:scikit-learn/scikit-learn.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/networkx.git",
        "upstream": "git@github.com:networkx/networkx.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/nx-guides.git",
        "upstream": "git@github.com:networkx/nx-guides.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/numpy.git",
        "upstream": "git@github.com:numpy/numpy.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/pandas.git",
        "upstream": "git@github.com:pandas-dev/pandas.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/cpython.git",
        "upstream": "git@github.com:python/cpython.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/machine-learning.git",
        "upstream": "git@github.com:ageron/handson-ml3.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/data-mining.git",
        "upstream": "git@github.com:zakimjz/dmbook-slides.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/PyMuPDF.git",
        "upstream": "git@github.com:pymupdf/PyMuPDF.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/jupyter.git",
        "upstream": "git@github.com:jupyter/jupyter.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/react.dev.git",
        "upstream": "git@github.com:reactjs/react.dev.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/TypeScript-Website.git",
        "upstream": "git@github.com:microsoft/TypeScript-Website.git",
        "upstream-default-branch": "v2"
    },
    {
        "fork": "git@github.com:QubitPi/babel-website.git",
        "upstream": "git@github.com:babel/website.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/redux.git",
        "upstream": "git@github.com:reduxjs/redux.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/react-redux.git",
        "upstream": "git@github.com:reduxjs/react-redux.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/redux-toolkit.git",
        "upstream": "git@github.com:reduxjs/redux-toolkit.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/immer.git",
        "upstream": "git@github.com:immerjs/immer.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/jest.git",
        "upstream": "git@github.com:jestjs/jest.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/testing-library-docs.git",
        "upstream": "git@github.com:testing-library/testing-library-docs.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/cypress-documentation.git",
        "upstream": "git@github.com:cypress-io/cypress-documentation.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/webpack.js.org.git",
        "upstream": "git@github.com:webpack/webpack.js.org.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/eslint-plugin-perfectionist.git",
        "upstream": "git@github.com:azat-io/eslint-plugin-perfectionist.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/3d-force-graph.git",
        "upstream": "git@github.com:vasturiano/3d-force-graph.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/react-force-graph.git",
        "upstream": "git@github.com:vasturiano/react-force-graph.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/lexical.git",
        "upstream": "git@github.com:facebook/lexical.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/docusaurus.git",
        "upstream": "git@github.com:facebook/docusaurus.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/inversify.github.io.git",
        "upstream": "git@github.com:inversify/inversify.github.io.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/logto-docs.git",
        "upstream": "git@github.com:logto-io/docs.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/arangodb-docs.git",
        "upstream": "git@github.com:arangodb/docs-hugo.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/arangodb-java-driver.git",
        "upstream": "git@github.com:arangodb/arangodb-java-driver.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/python-arango.git",
        "upstream": "git@github.com:arangodb/python-arango.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/docs-cypher.git",
        "upstream": "git@github.com:neo4j/docs-cypher.git",
        "upstream-default-branch": "dev"
    },
    {
        "fork": "git@github.com:QubitPi/neo4j-docs-drivers.git",
        "upstream": "git@github.com:neo4j/docs-drivers.git",
        "upstream-default-branch": "dev"
    },
    {
        "fork": "git@github.com:QubitPi/neo4j-java-driver.git",
        "upstream": "git@github.com:neo4j/neo4j-java-driver.git",
        "upstream-default-branch": "6.x"
    },
    {
        "fork": "git@github.com:QubitPi/neo4j-graph-examples-stackoverflow.git",
        "upstream": "git@github.com:neo4j-graph-examples/stackoverflow.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/neo4j-graph-examples-network-management.git",
        "upstream": "git@github.com:neo4j-graph-examples/network-management.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/neo4j-graph-examples-healthcare-analytics.git",
        "upstream": "git@github.com:neo4j-graph-examples/healthcare-analytics.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/neo4j-graph-examples-movies.git",
        "upstream": "git@github.com:neo4j-graph-examples/movies.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/hadoop.git",
        "upstream": "git@github.com:apache/hadoop.git",
        "upstream-default-branch": "trunk"
    },
    {
        "fork": "git@github.com:QubitPi/hbase.git",
        "upstream": "git@github.com:apache/hbase.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/hive.git",
        "upstream": "git@github.com:apache/hive.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/hive-doc.git",
        "upstream": "git@github.com:apache/hive-site.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/druid.git",
        "upstream": "git@github.com:apache/druid.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/druid-docs.git",
        "upstream": "git@github.com:apache/druid-website-src.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/openstack-nova.git",
        "upstream": "git@github.com:openstack/nova.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/openstack-swift.git",
        "upstream": "git@github.com:openstack/swift.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/openstack-python-swiftclient.git",
        "upstream": "git@github.com:openstack/python-swiftclient.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/javaswift.github.com.git",
        "upstream": "git@github.com:javaswift/javaswift.github.com.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/docker-swift-onlyone.git",
        "upstream": "git@github.com:FNNDSC/docker-swift-onlyone.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/elastic-docs-builder.git",
        "upstream": "git@github.com:elastic/docs-builder.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/elastic-stack-docs.git",
        "upstream": "git@github.com:elastic/stack-docs.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/elastic-docs.git",
        "upstream": "git@github.com:elastic/docs.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/cucumber-documentation.git",
        "upstream": "git@github.com:cucumber/website.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/reactivex-doc.git",
        "upstream": "git@github.com:ReactiveX/reactivex.github.io.git",
        "upstream-default-branch": "develop"
    },
    {
        "fork": "git@github.com:QubitPi/spock-doc.git",
        "upstream": "git@github.com:spockframework/spock.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/testcontainers-java.git",
        "upstream": "git@github.com:testcontainers/testcontainers-java.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/MailHog.git",
        "upstream": "git@github.com:mailhog/MailHog.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/docs.konghq.com.git",
        "upstream": "git@github.com:Kong/docs.konghq.com.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/ubuntu-server-documentation.git",
        "upstream": "git@github.com:canonical/ubuntu-server-documentation.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/sqlstyle.guide.git",
        "upstream": "git@github.com:treffynnon/sqlstyle.guide.git",
        "upstream-default-branch": "gh-pages"
    },
    {
        "fork": "git@github.com:QubitPi/jersey.git",
        "upstream": "git@github.com:eclipse-ee4j/jersey.git",
        "upstream-default-branch": "2.x"
    },
    {
        "fork": "git@github.com:QubitPi/jetty.project.git",
        "upstream": "git@github.com:jetty/jetty.project.git",
        "upstream-default-branch": "jetty-12.0.x"
    },
    {
        "fork": "git@github.com:QubitPi/gradle.git",
        "upstream": "git@github.com:gradle/gradle.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/kotlin-docs.git",
        "upstream": "git@github.com:JetBrains/kotlin-web-site.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/fastapi.git",
        "upstream": "git@github.com:fastapi/fastapi.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/jekyll-theme-jakarta-ee.git",
        "upstream": "git@github.com:jakartaee/jekyll-theme-jakarta-ee.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/jakartaee-rest.git",
        "upstream": "git@github.com:jakartaee/rest.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/jakartaee-persistence.git",
        "upstream": "git@github.com:jakartaee/persistence.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/hibernate-orm.git",
        "upstream": "git@github.com:hibernate/hibernate-orm.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/golang-website.git",
        "upstream": "git@github.com:golang/website.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/json-api.git",
        "upstream": "git@github.com:json-api/json-api.git",
        "upstream-default-branch": "gh-pages"
    },
    {
        "fork": "git@github.com:QubitPi/graphql-spec.git",
        "upstream": "git@github.com:graphql/graphql-spec.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/graphql-java-page.git",
        "upstream": "git@github.com:graphql-java/graphql-java-page.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/owner.git",
        "upstream": "git@github.com:matteobaccan/owner.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/hashicorp-dev-portal.git",
        "upstream": "git@github.com:hashicorp/dev-portal.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/hashicorp-packer.git",
        "upstream": "git@github.com:hashicorp/packer.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/hashicorp-terraform.git",
        "upstream": "git@github.com:hashicorp/terraform.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/hashicorp-vault.git",
        "upstream": "git@github.com:hashicorp/vault.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/hashicorp-consul.git",
        "upstream": "git@github.com:hashicorp/consul.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/packer-plugin-scaffolding.git",
        "upstream": "git@github.com:hashicorp/packer-plugin-scaffolding.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/terraform-provider-scaffolding-framework.git",
        "upstream": "git@github.com:hashicorp/terraform-provider-scaffolding-framework.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/docker-docs.git",
        "upstream": "git@github.com:docker/docs.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/docker-install.git",
        "upstream": "git@github.com:docker/docker-install.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/cadvisor.git",
        "upstream": "git@github.com:google/cadvisor.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/docker-mailserver.git",
        "upstream": "git@github.com:docker-mailserver/docker-mailserver.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/docker-kong.git",
        "upstream": "git@github.com:Kong/docker-kong.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/docker-registry-ui.git",
        "upstream": "git@github.com:Joxit/docker-registry-ui.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/linuxserver-documentation.git",
        "upstream": "git@github.com:linuxserver/docker-documentation.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/distribution.git",
        "upstream": "git@github.com:distribution/distribution.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/certbot.git",
        "upstream": "git@github.com:certbot/certbot.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/jenkins.io.git",
        "upstream": "git@github.com:jenkins-infra/jenkins.io.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/ansible-docs.git",
        "upstream": "git@github.com:ansible/docsite.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/docker-nexus3.git",
        "upstream": "git@github.com:sonatype/docker-nexus3.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/bats-core.git",
        "upstream": "git@github.com:bats-core/bats-core.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/writethedocs.git",
        "upstream": "git@github.com:writethedocs/www.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/diataxis-documentation-framework.git",
        "upstream": "git@github.com:evildmp/diataxis-documentation-framework.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/progit2.git",
        "upstream": "git@github.com:progit/progit2.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/keep-a-changelog.git",
        "upstream": "git@github.com:olivierlacan/keep-a-changelog.git",
        "upstream-default-branch": "main"
    },
    {
        "fork": "git@github.com:QubitPi/Bit-Twiddling-Hacks.git",
        "upstream": "git@github.com:virtyaluk/Bit-Twiddling-Hacks.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/github-repo-pins.git",
        "upstream": "git@github.com:anuraghazra/github-readme-stats.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/gravitational-wave-quickview.git",
        "upstream": "git@github.com:jkanner/streamlit-dataview.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/gravitational-wave-fitter.git",
        "upstream": "git@github.com:cardiffgravity/waveform-fitter.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:QubitPi/lottie2gif.git",
        "upstream": "git@github.com:lilas-dev/lottie2gif.git",
        "upstream-default-branch": "main"
    }
]

GENERATION_SOFTWARE_FORKS = [
    {
        "fork": "git@github.com:generation-software/screwdriver-cd-executor-docker.git",
        "upstream": "git@github.com:screwdriver-cd/executor-docker.git",
        "upstream-default-branch": "master"
    },
    {
        "fork": "git@github.com:generation-software/screwdriver-cd-guide.git",
        "upstream": "git@github.com:screwdriver-cd/guide.git",
        "upstream-default-branch": "master"
    }
]


# Credits to https://stackoverflow.com/a/65576165
class CloneProgress(RemoteProgress):
    def __init__(self):
        super().__init__()
        self.pbar = tqdm()

    def update(self, op_code, cur_count, max_count=None, message=''):
        self.pbar.total = max_count
        self.pbar.n = cur_count
        self.pbar.refresh()


def get_repo_name_from_git_url(url: str) -> str:
    """
    Credits to https://stackoverflow.com/a/55137835
    """
    last_slash_index = url.rfind("/")
    last_suffix_index = url.rfind(".git")
    if last_suffix_index < 0:
        last_suffix_index = len(url)

    if last_slash_index < 0 or last_suffix_index <= last_slash_index:
        raise Exception("Badly formatted url {}".format(url))

    return url[last_slash_index + 1:last_suffix_index]


def update_fork(forked_repo, upstream_repo, upstream_default_branch, forks_parent_dir="daily-sync"):
    forked_repo_name = get_repo_name_from_git_url(forked_repo)
    path = os.path.join(forks_parent_dir, forked_repo_name)

    if os.path.exists(path):
        print("{} already exists".format(path))
        fork = Repo(path)
        if "upstream" not in fork.remotes:
            fork.create_remote("upstream", upstream_repo)
    else:
        print("Cloning {} ...".format(forked_repo))
        try:
            fork = Repo.clone_from(
                url=forked_repo,
                to_path=path,
                progress=CloneProgress()
            )
        except GitCommandError as e:
            print(
                "Network error on cloning {forked_repo_name}. Retrying...\n".format(forked_repo_name=forked_repo_name))
            print(e)
            return False
        fork.create_remote("upstream", upstream_repo)

    upstream_remote = fork.remotes.upstream
    try:
        upstream_remote.fetch()
    except GitCommandError as e:
        print("Network error on fetching upstream of {forked_repo_name}. Retrying...".format(
            forked_repo_name=forked_repo_name))
        print(e)
        return False

    # check if upstram's default branch is equal to upstream_default_branch
    show_result = fork.git.remote("show", "upstream")
    matches = re.search(r"\s*HEAD branch:\s*(.*)", show_result)
    if matches:
        if upstream_default_branch != matches.group(1):
            print("⚠️ {}'s default branch changes to {} in upstream".format(forked_repo_name, matches.group(1)))
            return True

    try:
        print("Rebasing ...")
        fork.git.rebase("upstream/{branch}".format(branch=upstream_default_branch))
    except GitCommandError as e:
        if "CONFLICT" in str(e):
            print("⚠️ {fork} needs manual rebase".format(fork=forked_repo_name))
            print(e)
            return True  # done with this fork
        else:
            return True  # this should not be reached

    try:
        fork.remote("origin").push(refspec='master:master', force=True)
    except GitCommandError as e:
        print("Network error on pushing origin:master of {forked_repo_name}. Retrying...".format(
            forked_repo_name=forked_repo_name))
        print(e)
        return False

    return True


if __name__ == "__main__":
    for fork in FORKS:
        while not update_fork(fork["fork"], fork["upstream"], fork["upstream-default-branch"]):
            pass
    print("QubitPi forks sync done")

    for fork in GENERATION_SOFTWARE_FORKS:
        while not update_fork(
                fork["fork"],
                fork["upstream"],
                fork["upstream-default-branch"],
                os.path.join("daily-sync", "generation-software")
        ):
            pass
    print("Generation Software forks sync done")
