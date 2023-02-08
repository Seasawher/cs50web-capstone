FROM cs50web-capstone-django AS base

FROM cs50web-capstone-frontend
COPY --from=base /usr/local/ /usr/local/
