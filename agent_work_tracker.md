# Agent Work Tracker

This file tracks who is working on what and what stage each task is in.

## Roles
- Project Lead
- Delivery Coordinator
- Backend Engineer
- Frontend Coder
- Math and Logic Checker
- Compliance and Plan Reviewer
- Code Error Detector

## Status legend
- Not started
- In progress
- Blocked
- Ready for review
- Completed

## Current work board

| Task | Owner | Status | Notes |
|---|---|---|---|
| Project foundation and repo setup | Project Lead | Completed | Workspace and agent setup completed |
| Backend API creation | Backend Engineer | In progress | FastAPI route and simulation logic need final verification |
| Frontend dashboard redesign | Frontend Coder | In progress | UI is styled and build is passing |
| Math and forecast validation | Math and Logic Checker | Not started | Needs formula validation against plan |
| Compliance review against plan | Compliance and Plan Reviewer | Not started | Must validate against implementation_plan.md |
| Final code error sweep | Code Error Detector | Not started | Run after core features are integrated |
| Final demo readiness | Delivery Coordinator | Not started | End-to-end demo pass before final submission |

## Milestone checklist
- [ ] Backend simulation API working end-to-end
- [ ] Frontend dashboard polished and visually strong
- [ ] Data flow matches the plan
- [ ] Risk logic validated
- [ ] Compliance pass completed
- [ ] Final bug sweep passed
- [ ] Demo-ready flow confirmed

## Notes
- Agents are not autonomous background workers; they are invoked when selected in Copilot Chat.
- Use this tracker to manually maintain ownership and progress during the project.
