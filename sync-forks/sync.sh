#!/bin/bash
set -x
set -e

python3 sync.py -f git@github.com:QubitPi/leadership-blogs.git -u git@github.com:saicaca/fuwari.git -ub main
python3 sync.py -f git@github.com:QubitPi/wg-easy.git -u git@github.com:wg-easy/wg-easy.git -ub master
python3 sync.py -f git@github.com:QubitPi/mieru.git -u git@github.com:enfein/mieru.git -ub main
python3 sync.py -f git@github.com:QubitPi/writethedocs.git -u git@github.com:writethedocs/www.git -ub main # NS
python3 sync.py -f git@github.com:QubitPi/diataxis-documentation-framework.git -u git@github.com:evildmp/diataxis-documentation-framework.git -ub main

# ML
python3 sync.py -f git@github.com:QubitPi/mlflow.git -u git@github.com:mlflow/mlflow.git -ub master
python3 sync.py -f git@github.com:QubitPi/llama_index.git -u git@github.com:run-llama/llama_index.git -ub main
python3 sync.py -f git@github.com:QubitPi/ollama.git -u git@github.com:ollama/ollama.git -ub main
python3 sync.py -f git@github.com:QubitPi/openai-spinningup.git -u org-14957082@github.com:openai/spinningup.git -ub master
python3 sync.py -f git@github.com:QubitPi/scikit-learn.git -u git@github.com:scikit-learn/scikit-learn.git -ub main
python3 sync.py -f git@github.com:QubitPi/networkx.git -u git@github.com:networkx/networkx.git -ub main
python3 sync.py -f git@github.com:QubitPi/nx-guides.git -u git@github.com:networkx/nx-guides.git -ub main
python3 sync.py -f git@github.com:QubitPi/numpy.git -u git@github.com:numpy/numpy.git -ub main
python3 sync.py -f git@github.com:QubitPi/cpython.git -u git@github.com:python/cpython.git -ub main
python3 sync.py -f git@github.com:QubitPi/machine-learning.git -u git@github.com:ageron/handson-ml3.git -ub main
python3 sync.py -f git@github.com:QubitPi/data-mining.git -u git@github.com:zakimjz/dmbook-slides.git -ub master
python3 sync.py -f git@github.com:QubitPi/graphrag.git -u git@github.com:microsoft/graphrag.git -ub main
python3 sync.py -f git@github.com:QubitPi/PyMuPDF.git -u git@github.com:pymupdf/PyMuPDF.git -ub main

# UI
python3 sync.py -f git@github.com:QubitPi/react.dev.git -u git@github.com:reactjs/react.dev.git -ub main
python3 sync.py -f git@github.com:QubitPi/eslint-plugin-perfectionist.git -u git@github.com:azat-io/eslint-plugin-perfectionist.git -ub main # no-SEO: https://github.com/QubitPi/eslint-plugin-perfectionist/pull/2
python3 sync.py -f git@github.com:QubitPi/docusaurus.git -u git@github.com:facebook/docusaurus.git -ub main
python3 sync.py -f git@github.com:QubitPi/jest.git -u git@github.com:jestjs/jest.git -ub main
python3 sync.py -f git@github.com:QubitPi/cypress-documentation.git -u git@github.com:cypress-io/cypress-documentation.git -ub main
python3 sync.py -f git@github.com:QubitPi/redux.git -u git@github.com:reduxjs/redux.git -ub master
python3 sync.py -f git@github.com:QubitPi/react-redux.git -u git@github.com:reduxjs/react-redux.git -ub master
python3 sync.py -f git@github.com:QubitPi/redux-toolkit.git -u git@github.com:reduxjs/redux-toolkit.git -ub master
python3 sync.py -f git@github.com:QubitPi/babel-website.git -u git@github.com:babel/website.git -ub main
python3 sync.py -f git@github.com:QubitPi/TypeScript-Website.git -u git@github.com:microsoft/TypeScript-Website.git -ub v2
python3 sync.py -f git@github.com:QubitPi/3d-force-graph.git -u git@github.com:vasturiano/3d-force-graph.git -ub master
python3 sync.py -f git@github.com:QubitPi/react-force-graph.git -u git@github.com:vasturiano/react-force-graph.git -ub master

# Arango
python3 sync.py -f git@github.com:QubitPi/arangodb-docs.git -u git@github.com:arangodb/docs-hugo.git -ub main
python3 sync.py -f git@github.com:QubitPi/arangodb-java-driver.git -u git@github.com:arangodb/arangodb-java-driver.git -ub main
python3 sync.py -f git@github.com:QubitPi/python-arango.git -u git@github.com:arangodb/python-arango.git -ub main

# Hadoop Ecosystem
python3 sync.py -f git@github.com:QubitPi/hadoop.git -u git@github.com:apache/hadoop.git -ub trunk
python3 sync.py -f git@github.com:QubitPi/druid.git -u git@github.com:apache/druid.git -ub master # QubitPi/druid must sync before QubitPi/druid-docs
python3 sync.py -f git@github.com:QubitPi/druid-docs.git -u git@github.com:apache/druid-website-src.git -ub master

# OpenStack Ecosystem
python3 sync.py -f git@github.com:QubitPi/openstack-nova.git -u git@github.com:openstack/nova.git -ub master
python3 sync.py -f git@github.com:QubitPi/javaswift.github.com.git -u git@github.com:javaswift/javaswift.github.com.git -ub master
python3 sync.py -f git@github.com:QubitPi/docker-swift-onlyone.git -u git@github.com:FNNDSC/docker-swift-onlyone.git -ub master

# ELK
# python3 sync.py -f git@github.com:QubitPi/logstash.git -u git@github.com:elastic/logstash.git -ub main

# Backend
python3 sync.py -f git@github.com:QubitPi/spock-doc.git -u git@github.com:spockframework/spock.git -ub master
python3 sync.py -f git@github.com:QubitPi/testcontainers-java.git -u git@github.com:testcontainers/testcontainers-java.git -ub main
python3 sync.py -f git@github.com:QubitPi/MailHog.git -u git@github.com:mailhog/MailHog.git -ub master
python3 sync.py -f git@github.com:QubitPi/docs.konghq.com.git -u git@github.com:Kong/docs.konghq.com.git -ub main
python3 sync.py -f git@github.com:QubitPi/ubuntu-server-documentation.git -u git@github.com:canonical/ubuntu-server-documentation.git -ub main
python3 sync.py -f git@github.com:QubitPi/sqlstyle.guide.git -u git@github.com:treffynnon/sqlstyle.guide.git -ub gh-pages
python3 sync.py -f git@github.com:QubitPi/jersey.git -u git@github.com:eclipse-ee4j/jersey.git -ub 2.x
python3 sync.py -f git@github.com:QubitPi/jetty.project.git -u git@github.com:jetty/jetty.project.git -ub jetty-12.0.x
python3 sync.py -f git@github.com:QubitPi/gradle.git -u git@github.com:gradle/gradle.git -ub master
python3 sync.py -f git@github.com:QubitPi/kotlin-docs.git -u git@github.com:JetBrains/kotlin-web-site.git -ub master

python3 sync.py -f git@github.com:QubitPi/fastapi.git -u git@github.com:fastapi/fastapi.git -ub master
python3 sync.py -f git@github.com:QubitPi/jekyll-theme-jakarta-ee.git -u git@github.com:jakartaee/jekyll-theme-jakarta-ee.git -ub master
python3 sync.py -f git@github.com:QubitPi/jakartaee-rest.git -u git@github.com:jakartaee/rest.git -ub main
python3 sync.py -f git@github.com:QubitPi/golang-website.git -u git@github.com:golang/website.git -ub master

# HashiCorp
# ⚠️ hashicorp-dev-portal must sync first
python3 sync.py -f git@github.com:QubitPi/hashicorp-dev-portal.git -u git@github.com:hashicorp/dev-portal.git -ub main
python3 sync.py -f git@github.com:QubitPi/hashicorp-packer.git -u git@github.com:hashicorp/packer.git -ub main
python3 sync.py -f git@github.com:QubitPi/hashicorp-terraform.git -u git@github.com:hashicorp/terraform.git -ub main
python3 sync.py -f git@github.com:QubitPi/hashicorp-vault.git -u git@github.com:hashicorp/vault.git -ub main
python3 sync.py -f git@github.com:QubitPi/hashicorp-consul.git -u git@github.com:hashicorp/consul.git -ub main

# Docker
python3 sync.py -f git@github.com:QubitPi/docker-docs.git -u git@github.com:docker/docs.git -ub main # no-SEO: https://github.com/QubitPi/docker-docs/pull/6
python3 sync.py -f git@github.com:QubitPi/docker-install.git -u git@github.com:docker/docker-install.git -ub master
python3 sync.py -f git@github.com:QubitPi/cadvisor.git -u git@github.com:google/cadvisor.git -ub master
python3 sync.py -f git@github.com:QubitPi/docker-mailserver.git -u git@github.com:docker-mailserver/docker-mailserver.git -ub master
python3 sync.py -f git@github.com:QubitPi/docker-kong.git -u git@github.com:Kong/docker-kong.git -ub master
python3 sync.py -f git@github.com:QubitPi/docker-registry-ui.git -u git@github.com:Joxit/docker-registry-ui.git -ub main
python3 sync.py -f git@github.com:QubitPi/linuxserver-documentation.git -u git@github.com:linuxserver/docker-documentation.git -ub master # NS

# DevOps
python3 sync.py -f git@github.com:QubitPi/certbot.git -u git@github.com:certbot/certbot.git -ub main

python3 sync.py -f git@github.com:QubitPi/progit2.git -u git@github.com:progit/progit2.git -ub main
python3 sync.py -f git@github.com:QubitPi/Bit-Twiddling-Hacks.git -u git@github.com:virtyaluk/Bit-Twiddling-Hacks.git -ub master
