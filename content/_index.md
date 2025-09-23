---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: collection
    id: posts
    content:
      title: Latest Writing
      subtitle: Research notes and essays on artificial intelligence, robotics, and language technologies.
      text: >-
        Welcome to my lab notebook. Dive into the newest articles below or explore the complete archive on the <a href="/post/">blog page</a>.
      filters:
        folders:
          - post
      count: 6
      sort_by: date
      order: desc
    design:
      view: article
      columns: '1'
  - block: about.avatar
    id: about
    content:
      title: Meet Alice
      username: admin
      text: >-
        I study how intelligent systems learn, reason, and interact in the physical world. When I'm not teaching, I'm writing to untangle complex ideas for a broader audience. Get the full story on the <a href="/about/">about page</a>.
    design:
      columns: '2'
  - block: collection
    id: projects
    content:
      title: Selected Projects
      subtitle: A rotating sample of lab work and collaborations.
      filters:
        folders:
          - project
      count: 3
    design:
      view: showcase
      columns: '1'
      flip_alt_rows: false
  - block: collection
    id: publications
    content:
      title: Recent Publications
      text: Browse the full bibliography on the <a href="/publication/">publications page</a>.
      filters:
        folders:
          - publication
        exclude_featured: false
      count: 6
    design:
      view: citation
      columns: '2'
  - block: markdown
    id: stay-in-touch
    content:
      title: Stay in touch
      subtitle: Occasional updates on new essays and research.
      text: >-
        Prefer updates in your inbox? Subscribe to the RSS feed or reach out directly through the <a href="/contact/">contact page</a>.
    design:
      columns: '1'
---
