

## meetup
https://www.meetup.com/find/?location=gb--17--London--Islington&source=EVENTS&distance=tenMiles

see:
https://stackoverflow.com/questions/54994689/web-scraping-when-scrolling-down-is-needed
https://stackoverflow.com/questions/22702277/crawl-site-that-has-infinite-scrolling-using-python
https://stackoverflow.com/questions/27775759/send-keys-control-click-in-selenium-with-python-bindings
https://stackoverflow.com/questions/75467250/how-to-scrape-the-link-of-all-links-from-a-webpage-and-scroll-down
https://www.accordbox.com/blog/how-crawl-infinite-scrolling-pages-using-python/

```html

<div>
    <div data-recommendationid="fbc1dbb2-12ae-49f2-b78f-60e002a3b5f4"
         data-recommendationsource="ml-popular-events-nearby" data-eventref="294724747"
         data-element-name="categoryResults-eventCard" data-testid="categoryResults-eventCard"
         class="p-0 bg-clip-padding bg-cover bg-transparent relative h-full flex bg-white z-0 break-words transition-shadow duration-300 w-full flex-row justify-start py-4 border-t border-gray3 md:pt-4 md:pb-5">
        <a class="w-full inline cursor-pointer relative hover:no-underline"
           href="https://www.meetup.com/product-management-careers-uk/events/294724747/" data-event-label="Event card"
           id="event-card-in-search-results">
            <div class="flex w-full flex-col">
                <div class="flex flex-row-reverse md:flex-row flex-1 overflow-hidden">
                    <div class="bg-transparent ml-3 md:mr-3 md:ml-0 d15a685b">
                        <div class="relative overflow-hidden bg-transparent w-full" style="height: 125px;">
                            <picture>
                                <source srcset="https://secure.meetupstatic.com/photos/event/4/0/0/6/event_514336390.jpeg, https://secure.meetupstatic.com/photos/event/4/0/0/6/event_514336390.jpeg 1.5x, https://secure.meetupstatic.com/photos/event/4/0/0/6/event_514336390.jpeg 2x"
                                        type="image/webp">
                                <source srcset="https://secure.meetupstatic.com/photos/event/4/0/0/6/event_514336390.jpeg, https://secure.meetupstatic.com/photos/event/4/0/0/6/event_514336390.jpeg 1.5x, https://secure.meetupstatic.com/photos/event/4/0/0/6/event_514336390.jpeg 2x"
                                        type="image/jpeg">
                                <img src="https://secure.meetupstatic.com/photos/event/4/0/0/6/event_514336390.jpeg"
                                     width="222" height="125"
                                     alt="How to be the product manager UK employers are looking to hire" loading="lazy"
                                     class="rounded-t-lg rounded-lg w-full absolute top-0 left-0 object-contain object-center">
                            </picture>
                            <div class="absolute top-2 left-2 right-2 hidden md:flex" aria-label="Online Event"
                                 data-testid="online-indicator">
                                <div class="flex flex-row items-center z-10 text-xs rounded font-medium truncate py-0.5 pr-2 pl-1 bg-white">
                                    <div class="mr-1" data-icon-c="icon-41" style="width: 16px; height: 16px;">
                                        <div>
                                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24"
                                                 viewBox="0 0 24 24" fill="none"
                                                 class="injected-svg text-gray6 fill-current"
                                                 data-src="https://secure.meetupstatic.com/next/images/design-system-icons/video.svg"
                                                 xmlns:xlink="http://www.w3.org/1999/xlink"
                                                 style="width:16px;height:16px;width:16px;height:16px"
                                                 data-icon="icon-41"><title>icon</title>
                                                <path fill-rule="evenodd" clip-rule="evenodd"
                                                      d="M4 4C2.89543 4 2 4.89543 2 6V18C2 19.1046 2.89543 20 4 20H14C15.1046 20 16 19.1046 16 18V15.1869C16 15.107 16.089 15.0593 16.1555 15.1036L20.4453 17.9635C21.1099 18.4066 22 17.9302 22 17.1315V6.86852C22 6.06982 21.1099 5.59343 20.4453 6.03647L16.1555 8.89635C16.089 8.94066 16 8.89302 16 8.81315V6C16 4.89543 15.1046 4 14 4H4Z"></path>
                                            </svg>
                                        </div>
                                    </div>
                                    <span class="text-gray6 truncate">Online Event</span></div>
                            </div>
                        </div>
                    </div>
                    <div class="overflow-hidden w-full">
                        <div class="flex justify-between md:items-center flex-col-reverse md:flex-row">
                            <div class="flex flex-col uppercase text-sm leading-5 tracking-tight text-darkGold font-medium pb-1 pt-1 line-clamp-1 lg:line-clamp-2">
                                <h3>
                                    <time class="" datetime="2023-07-18T13:00:00+01:00[Europe/London]"
                                          title="Tue Jul 18 2023 13:00:00 GMT+0100 (British Summer Time)">Tue, Jul 18 ·
                                        1:00 PM BST
                                    </time>
                                </h3>
                            </div>
                        </div>
                        <h2 class="text-gray7 font-medium text-base pt-0 pb-1 line-clamp-3">How to be the product
                            manager UK employers are looking to hire</h2>
                        <div class="w-full  text-sm  mx-auto mb-2 md:mb-4"><p class="hidden md:line-clamp-1 text-gray6">
                            <span class="s1uol3r6">Group name:</span>Product Management Careers UK • London, 17</p>
                            <p class="hidden md:line-clamp-1 text-viridian ">New Group</p>
                            <p class="line-clamp-1 md:hidden"><span class="s1uol3r6">Group name:</span>Product
                                Management Careers UK</p>
                            <p class="line-clamp-1 md:hidden">London, 17</p>
                            <p class="line-clamp-1 md:hidden text-viridian pt-[2px]">New Group</p></div>
                        <div class="h-0 sm:h-8 hidden sm:block xmedia">
                            <div class="h-full w-full flex items-end">
                                <div class="w-full flex flex-col">
                                    <div class="flex items-center">
                                        <div class="flex flex-row">
                                            <div class="text-gray6 text-sm">
                                                <div aria-label="56 attendees" class="text-gray6 text-sm">56 attendees
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="md:hidden xs:p-0 mt-1" aria-label="Online Event"
                                         data-testid="online-indicator">
                                        <div class="flex flex-row items-center z-10 text-xs rounded font-medium truncate py-0.5 pr-2 pl-1 bg-white">
                                            <div class="mr-1" data-icon-c="icon-53" style="width: 16px; height: 16px;">
                                                <div>
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24"
                                                         viewBox="0 0 24 24" fill="none"
                                                         class="injected-svg text-gray6 fill-current"
                                                         data-src="https://secure.meetupstatic.com/next/images/design-system-icons/video.svg"
                                                         xmlns:xlink="http://www.w3.org/1999/xlink"
                                                         style="width:16px;height:16px;width:16px;height:16px"
                                                         data-icon="icon-53"><title>icon</title>
                                                        <path fill-rule="evenodd" clip-rule="evenodd"
                                                              d="M4 4C2.89543 4 2 4.89543 2 6V18C2 19.1046 2.89543 20 4 20H14C15.1046 20 16 19.1046 16 18V15.1869C16 15.107 16.089 15.0593 16.1555 15.1036L20.4453 17.9635C21.1099 18.4066 22 17.9302 22 17.1315V6.86852C22 6.06982 21.1099 5.59343 20.4453 6.03647L16.1555 8.89635C16.089 8.94066 16 8.89302 16 8.81315V6C16 4.89543 15.1046 4 14 4H4Z"></path>
                                                    </svg>
                                                </div>
                                            </div>
                                            <span class="text-gray6 truncate">Online Event</span></div>
                                    </div>
                                </div>
                                <div class="flex h-8 relative"></div>
                                <div class="flex items-center h-8 z-10 gap-3">
                                    <button class="fill-current text-gray6 hover:text-gray7"
                                            aria-label="Share event How to be the product manager UK employers are looking to hire"
                                            tabindex="0" data-element-name="categorySearch-share-click"
                                            data-event-label="Share icon" data-testid="share-btn">
                                        <div class="flex items-center">
                                            <div data-element-name="share-in-event-search-results"
                                                 data-icon-c="icon-54">
                                                <div>
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24"
                                                         viewBox="0 0 24 24" fill="none"
                                                         class="injected-svg fill-current"
                                                         data-src="https://secure.meetupstatic.com/next/images/design-system-icons/share-outline.svg"
                                                         xmlns:xlink="http://www.w3.org/1999/xlink" data-icon="icon-54">
                                                        <title>icon</title>
                                                        <path fill-rule="evenodd" clip-rule="evenodd"
                                                              d="M10.8232 5.23741C10.9807 5.07992 11.25 5.19146 11.25 5.41419L11.25 14.25C11.25 14.6642 11.5858 15 12 15C12.4142 15 12.75 14.6642 12.75 14.25V5.41418C12.75 5.19146 13.0193 5.07992 13.1768 5.23741L15.9697 8.0303C16.2626 8.32319 16.7374 8.32319 17.0303 8.0303C17.3232 7.73741 17.3232 7.26253 17.0303 6.96964L13.2374 3.17675C12.554 2.49333 11.446 2.49333 10.7626 3.17675L6.96967 6.96964C6.67678 7.26253 6.67678 7.73741 6.96967 8.0303C7.26256 8.32319 7.73744 8.32319 8.03033 8.0303L10.8232 5.23741ZM9.25 10H6C4.89543 10 4 10.8954 4 12V20C4 21.1046 4.89543 22 6 22H18C19.1046 22 20 21.1046 20 20V12C20 10.8954 19.1046 10 18 10H14.75V11.5H18C18.2761 11.5 18.5 11.7239 18.5 12V20C18.5 20.2761 18.2761 20.5 18 20.5H6C5.72386 20.5 5.5 20.2761 5.5 20V12C5.5 11.7239 5.72386 11.5 6 11.5H9.25V10Z"></path>
                                                    </svg>
                                                </div>
                                            </div>
                                        </div>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="h-8 mt-1.5 sm:h-0 sm:mt-0 block sm:hidden xmedia"></div>
            </div>
        </a></div>
</div>
```

## event bright

https://www.eventbrite.co.uk/d/united-kingdom--london/free--events--this-weekend/meet-up/?page=1&cur=GBP&lang=en

```html
<li class="search-main-content__events-list-item">
    <div data-testid="search-event" role="presentation">
        <div class="discover-search-mobile-card">
            <section class="discover-horizontal-event-card">
                <div class="Container_root__16e3w NestedActionContainer_root__1jtfr event-card event-card__horizontal"
                     style="--ContainerBgColor: #fff; --ContainerBorderRadius: 16px; --ContainerElevationFocusWithin: 0px 2px 8px rgba(30, 10, 60, 0.06), 0px 4px 12px rgba(30, 10, 60, 0.08); --ContainerElevationHover: 0px 2px 8px rgba(30, 10, 60, 0.06), 0px 4px 12px rgba(30, 10, 60, 0.08); --ContainerPadding: 16px;">
                    <div data-testid="event-card-tracking-layer" data-event-id="658500351277"
                         data-event-location="London, England" data-event-paid-status="free"
                         data-event-category="community"
                         style="position: absolute; top: 0px; left: 0px; height: 100%; pointer-events: none; width: 100%;"></div>
                    <section class="event-card-details" style="--EventCardDetailsPadding: 0 16px 0 0;">
                        <div class="Stack_root__1ksk7" style="--Space: 8px;"><a
                                href="https://www.eventbrite.co.uk/e/make-long-term-friends-tickets-658500351277?aff=ebdssbdestsearch"
                                rel="noopener" target="_blank" class="event-card-link "
                                aria-label="View Make long term friends!" data-airgap-id="801"><h2
                                class="Typography_root__4bejd #585163 Typography_body-lg__4bejd event-card__clamp-line--three Typography_align-match-parent__4bejd"
                                style="--TypographyColor: #585163;">Make long term friends!</h2></a>
                            <p class="Typography_root__4bejd #585163 Typography_body-md-bold__4bejd eds-text-color--primary-brand Typography_align-match-parent__4bejd"
                               style="--TypographyColor: #585163;">Sunday at 16:00</p>
                            <p class="Typography_root__4bejd #585163 Typography_body-md__4bejd event-card__clamp-line--one Typography_align-match-parent__4bejd"
                               style="--TypographyColor: #585163;">Furnivall Gardens • London</p>
                            <p class="Typography_root__4bejd #585163 Typography_body-md__4bejd Typography_align-match-parent__4bejd"
                               style="--TypographyColor: #585163;">Free</p></div>
                    </section>
                    <section class="horizontal-event-card__column"><a
                            href="https://www.eventbrite.co.uk/e/make-long-term-friends-tickets-658500351277?aff=ebdssbdestsearch"
                            rel="noopener" target="_blank" class="event-card-link "
                            aria-label="View Make long term friends!" data-airgap-id="802">
                        <div class="event-card-image__aspect-container"
                             style="--image-aspect-ratio: 2; --image-aspect-ratio-mobile: 1; --image-width: 220px; --image-width-mobile: 100px; --image-background-color: #7595ab;">
                            <img height="256" width="512" class="event-card-image"
                                 src="https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F535858249%2F1488100049313%2F1%2Foriginal.20230614-151142?w=512&amp;auto=format%2Ccompress&amp;q=75&amp;sharp=10&amp;rect=0%2C71%2C874%2C437&amp;s=964ea30f579d4eb0dee754e907063139"
                                 loading="lazy" alt="Make long term friends! primary image" data-airgap-id="803"></div>
                    </a>
                        <section class="event-card-actions" style="--EventCardActionsMargin: 12px 0 0 0;"><span
                                class="eds-icon-button eds-icon-button--neutral" data-spec="icon-button"><button
                                class="eds-btn--button eds-btn--none eds-btn--icon-only" type="button"><i
                                class="eds-vector-image eds-icon--small eds-vector-image--block" title=""
                                data-spec="icon" data-testid="icon"><svg id="share-ios-chunky_svg__eds-icon--share-ios-chunky_svg" x="0" y="0" viewBox="0 0 24 24" xml:space="preserve"><path id="share-ios-chunky_svg__eds-icon--share-ios-chunky_base" fill-rule="evenodd" clip-rule="evenodd" d="M18 16v2H6v-2H4v4h16v-4z"></path><path
                                id="share-ios-chunky_svg__eds-icon--share-ios-chunky_arrow" fill-rule="evenodd"
                                clip-rule="evenodd" d="M12 4L7 9l1.4 1.4L11 7.8V16h2V7.8l2.6 2.6L17 9l-5-5z"></path></svg><span
                                class="eds-is-hidden-accessible">Share this event</span></i></button></span>
                            <div class="test"><span class="eds-icon-button eds-icon-button--neutral"
                                                    data-spec="icon-button"><button aria-pressed="false"
                                                                                    data-event-id="658500351277"
                                                                                    class="eds-btn--button eds-btn--none eds-btn--icon-only"
                                                                                    type="button"><i
                                    class="eds-vector-image eds-icon--small eds-vector-image--grey-700 eds-vector-image--block"
                                    title="" data-spec="icon" data-testid="icon"><svg id="heart-chunky_svg__eds-icon--user-chunky_svg" x="0" y="0" viewBox="0 0 24 24" xml:space="preserve"><path id="heart-chunky_svg__eds-icon--heart-chunky_base" fill-rule="evenodd" clip-rule="evenodd" d="M18.8 6.2C18.1 5.4 17 5 16 5c-1 0-2 .4-2.8 1.2L12 7.4l-1.2-1.2C10 5.4 9 5 8 5c-1 0-2 .4-2.8 1.2-1.5 1.6-1.5 4.2 0 5.8l6.8 7 6.8-7c1.6-1.6 1.6-4.2 0-5.8zm-1.4 4.4L12 16.1l-5.4-5.5c-.8-.8-.8-2.2 0-3C7 7.2 7.5 7 8 7c.5 0 1 .2 1.4.6l2.6 2.7 2.7-2.7c.3-.4.8-.6 1.3-.6s1 .2 1.4.6c.8.8.8 2.2 0 3z"></path></svg><span
                                    class="eds-is-hidden-accessible">Save this event: Make long term friends!</span></i></button></span>
                            </div>
                        </section>
                    </section>
                </div>
            </section>
        </div>
        <div class="discover-search-desktop-card">
            <section class="discover-horizontal-event-card">
                <div class="Container_root__16e3w NestedActionContainer_root__1jtfr event-card event-card__horizontal horizontal-event-card__action-visibility"
                     style="--ContainerBgColor: #fff; --ContainerBorderRadius: 16px; --ContainerElevationFocusWithin: 0px 2px 8px rgba(30, 10, 60, 0.06), 0px 4px 12px rgba(30, 10, 60, 0.08); --ContainerElevationHover: 0px 2px 8px rgba(30, 10, 60, 0.06), 0px 4px 12px rgba(30, 10, 60, 0.08); --ContainerPadding: 16px;">
                    <div data-testid="event-card-tracking-layer" data-event-id="658500351277"
                         data-event-location="London, England" data-event-paid-status="free"
                         data-event-category="community"
                         style="position: absolute; top: 0px; left: 0px; height: 100%; pointer-events: none; width: 100%;"></div>
                    <section class="event-card-details"
                             style="--EventCardDetailsPadding: 0 16px 0 0; --EventCardDetailsFlexGrow: 2;">
                        <div class="Stack_root__1ksk7" style="--Space: 8px;"><a
                                href="https://www.eventbrite.co.uk/e/make-long-term-friends-tickets-658500351277?aff=ebdssbdestsearch"
                                rel="noopener" target="_blank" class="event-card-link "
                                aria-label="View Make long term friends!" data-airgap-id="806"><h2
                                class="Typography_root__4bejd #585163 Typography_body-lg__4bejd event-card__clamp-line--two Typography_align-match-parent__4bejd"
                                style="--TypographyColor: #585163;">Make long term friends!</h2></a>
                            <p class="Typography_root__4bejd #585163 Typography_body-md__4bejd event-card__clamp-line--one eds-text-color--ui-600 Typography_align-match-parent__4bejd"
                               style="margin-top: 4px;">Sunday at 16:00</p>
                            <p class="Typography_root__4bejd #585163 Typography_body-md__4bejd event-card__clamp-line--one eds-text-color--ui-600 Typography_align-match-parent__4bejd"
                               style="margin-top: 4px;">Furnivall Gardens</p>
                            <p class="Typography_root__4bejd #585163 Typography_body-md-bold__4bejd Typography_align-match-parent__4bejd"
                               style="margin-top: 8px;">Free</p>
                            <section class="event-card-actions" style="--EventCardActionsMargin: 12px 0 0 0;"><span
                                    class="eds-icon-button eds-icon-button--neutral" data-spec="icon-button"><button
                                    class="eds-btn--button eds-btn--none eds-btn--icon-only" type="button"><i
                                    class="eds-vector-image eds-icon--small eds-vector-image--block" title=""
                                    data-spec="icon" data-testid="icon"><svg id="share-ios-chunky_svg__eds-icon--share-ios-chunky_svg" x="0" y="0" viewBox="0 0 24 24" xml:space="preserve"><path id="share-ios-chunky_svg__eds-icon--share-ios-chunky_base" fill-rule="evenodd" clip-rule="evenodd" d="M18 16v2H6v-2H4v4h16v-4z"></path><path
                                    id="share-ios-chunky_svg__eds-icon--share-ios-chunky_arrow" fill-rule="evenodd"
                                    clip-rule="evenodd" d="M12 4L7 9l1.4 1.4L11 7.8V16h2V7.8l2.6 2.6L17 9l-5-5z"></path></svg><span
                                    class="eds-is-hidden-accessible">Share this event</span></i></button></span>
                                <div class="test"><span class="eds-icon-button eds-icon-button--neutral"
                                                        data-spec="icon-button"><button aria-pressed="false"
                                                                                        data-event-id="658500351277"
                                                                                        class="eds-btn--button eds-btn--none eds-btn--icon-only"
                                                                                        type="button"><i
                                        class="eds-vector-image eds-icon--small eds-vector-image--grey-700 eds-vector-image--block"
                                        title="" data-spec="icon" data-testid="icon"><svg id="heart-chunky_svg__eds-icon--user-chunky_svg" x="0" y="0" viewBox="0 0 24 24" xml:space="preserve"><path id="heart-chunky_svg__eds-icon--heart-chunky_base" fill-rule="evenodd" clip-rule="evenodd" d="M18.8 6.2C18.1 5.4 17 5 16 5c-1 0-2 .4-2.8 1.2L12 7.4l-1.2-1.2C10 5.4 9 5 8 5c-1 0-2 .4-2.8 1.2-1.5 1.6-1.5 4.2 0 5.8l6.8 7 6.8-7c1.6-1.6 1.6-4.2 0-5.8zm-1.4 4.4L12 16.1l-5.4-5.5c-.8-.8-.8-2.2 0-3C7 7.2 7.5 7 8 7c.5 0 1 .2 1.4.6l2.6 2.7 2.7-2.7c.3-.4.8-.6 1.3-.6s1 .2 1.4.6c.8.8.8 2.2 0 3z"></path></svg><span
                                        class="eds-is-hidden-accessible">Save this event: Make long term friends!</span></i></button></span>
                                </div>
                            </section>
                        </div>
                    </section>
                    <section class="horizontal-event-card__column" style="--HorizontalCardColumnMarginRight: 24px;"><a
                            href="https://www.eventbrite.co.uk/e/make-long-term-friends-tickets-658500351277?aff=ebdssbdestsearch"
                            rel="noopener" target="_blank" class="event-card-link "
                            aria-label="View Make long term friends!" data-airgap-id="804">
                        <div class="event-card-image__aspect-container"
                             style="--image-aspect-ratio: 2; --image-aspect-ratio-mobile: 1; --image-width: 220px; --image-width-mobile: 100px; --image-background-color: #7595ab;">
                            <img height="256" width="512" class="event-card-image"
                                 src="https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F535858249%2F1488100049313%2F1%2Foriginal.20230614-151142?w=512&amp;auto=format%2Ccompress&amp;q=75&amp;sharp=10&amp;rect=0%2C71%2C874%2C437&amp;s=964ea30f579d4eb0dee754e907063139"
                                 loading="lazy" alt="Make long term friends! primary image" data-airgap-id="805"></div>
                    </a></section>
                </div>
            </section>
        </div>
    </div>
</li>
```

